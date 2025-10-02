"""
Taken from https://github.com/fra31/auto-attack

MIT License
"""
import math
import time
from typing import Callable, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


def L0_norm(x: torch.Tensor) -> torch.Tensor:
    """
    Calculate the L0 norm of a tensor.

    Args:
        x (torch.Tensor): Input tensor.

    Returns:
        torch.Tensor: The L0 norm of the input tensor.
    """
    return (x != 0.).view(x.shape[0], -1).sum(-1)


def L1_norm(x: torch.Tensor, keepdim: bool = False) -> torch.Tensor:
    """
    Calculate the L1 norm of a tensor.

    Args:
        x (torch.Tensor): Input tensor.
        keepdim (bool, optional): Whether to keep the dimensions or not. Defaults to False.

    Returns:
        torch.Tensor: The L1 norm of the input tensor.
    """
    z = x.abs().view(x.shape[0], -1).sum(-1)
    if keepdim:
        z = z.view(-1, *[1] * (len(x.shape) - 1))
    return z


def L2_norm(x: torch.Tensor, keepdim: bool = False) -> torch.Tensor:
    """
    Calculate the L2 norm of a tensor.

    Args:
        x (torch.Tensor): Input tensor.
        keepdim (bool, optional): Whether to keep the dimensions or not. Defaults to False.

    Returns:
        torch.Tensor: The L2 norm of the input tensor.
    """
    z = (x ** 2).view(x.shape[0], -1).sum(-1).sqrt()
    if keepdim:
        z = z.view(-1, *[1] * (len(x.shape) - 1))
    return z


def L1_projection(x2: torch.Tensor, y2: torch.Tensor, eps1: float) -> torch.Tensor:
    """
    Project a point onto an L1 ball.

    Args:
        x2 (torch.Tensor): Center of the L1 ball (bs x input_dim).
        y2 (torch.Tensor): Current perturbation (x2 + y2 is the point to be projected).
        eps1 (float): Radius of the L1 ball.

    Returns:
        torch.Tensor: Delta such that ||y2 + delta||_1 <= eps1 and 0 <= x2 + y2 + delta <= 1.
    """
    x = x2.clone().float().view(x2.shape[0], -1)
    y = y2.clone().float().view(y2.shape[0], -1)
    sigma = y.clone().sign()
    u = torch.min(1 - x - y, x + y)
    u = torch.min(torch.zeros_like(y), u)
    lvar = -torch.clone(y).abs()
    d = u.clone()
    bs, indbs = torch.sort(-torch.cat((u, lvar), 1), dim=1)
    bs2 = torch.cat((bs[:, 1:], torch.zeros(bs.shape[0], 1).to(bs.device)), 1)
    inu = 2 * (indbs < u.shape[1]).float() - 1
    size1 = inu.cumsum(dim=1)
    s1 = -u.sum(dim=1)
    c = eps1 - y.clone().abs().sum(dim=1)
    c5 = s1 + c < 0
    c2 = c5.nonzero().squeeze(1)
    s = s1.unsqueeze(-1) + torch.cumsum((bs2 - bs) * size1, dim=1)

    if c2.nelement != 0:
        lb = torch.zeros_like(c2).float()
        ub = torch.ones_like(lb) * (bs.shape[1] - 1)

        nitermax = torch.ceil(torch.log2(torch.tensor(bs.shape[1]).float()))
        counter2 = torch.zeros_like(lb).long()
        counter = 0
        while counter < nitermax:
            counter4 = torch.floor((lb + ub) / 2.)
            counter2 = counter4.type(torch.LongTensor)
            c8 = s[c2, counter2] + c[c2] < 0
            ind3 = c8.nonzero().squeeze(1)
            ind32 = (~c8).nonzero().squeeze(1)
            if ind3.nelement != 0:
                lb[ind3] = counter4[ind3]
            if ind32.nelement != 0:
                ub[ind32] = counter4[ind32]
            counter += 1
        lb2 = lb.long()
        alpha = (-s[c2, lb2] - c[c2]) / size1[c2, lb2 + 1] + bs2[c2, lb2]
        d[c2] = -torch.min(torch.max(-u[c2], alpha.unsqueeze(-1)), -lvar[c2])
    return (sigma * d).view(x2.shape)


class APGDAttack:
    """
    Implements the Auto-PGD (Auto Projected Gradient Descent) attack method.

    Attributes:
        model (Callable): A function representing the forward pass of the model to be attacked.
        n_iter (int): Number of iterations for the attack.
        norm (str): The type of norm for the attack ('Linf', 'L2', 'L1').
        n_restarts (int): Number of random restarts for the attack.
        eps (float): The maximum perturbation amount allowed.
        seed (int): Random seed for reproducibility.
        loss (str): Type of loss function to use ('ce' for cross-entropy, 'dlr').
        eot_iter (int): Number of iterations for Expectation over Transformation.
        rho (float): Parameter for adjusting step size.
        topk (Optional[float]): Parameter for controlling the sparsity of the attack.
        verbose (bool): If True, prints verbose output during the attack.
        device (Optional[torch.device]): The device on which to perform computations.
        use_largereps (bool): If True, uses larger epsilon values in initial iterations.
        is_tf_model (bool): If True, indicates the model is a TensorFlow model.

    Methods:
        init_hyperparam(x): Initializes hyperparameters based on the input data.
        check_oscillation(...): Checks for oscillation in the optimization process.
        check_shape(x): Ensures the input has the expected shape.
        normalize(x): Normalizes the input tensor.
        lp_norm(x): Computes the Lp norm of the input.
        dlr_loss(x, y): Computes the Deep Learning Robustness (DLR) loss.
        attack_single_run(x, y, x_init=None): Performs a single run of the attack.
        perturb(x, y=None, best_loss=False, x_init=None): Generates adversarial examples for the given inputs.
        decr_eps_pgd(x, y, epss, iters, use_rs=True): Performs PGD with decreasing epsilon values.
    """
    def __init__(
            self,
            predict: Callable,
            n_iter: int = 100,
            norm: str = 'Linf',
            n_restarts: int = 1,
            eps: Optional[float] = None,
            seed: int = 0,
            loss: str = 'ce',
            eot_iter: int = 1,
            rho: float = .75,
            topk: Optional[float] = None,
            verbose: bool = False,
            device: Optional[torch.device] = None,
            use_largereps: bool = False,
            is_tf_model: bool = False):
        """
        Initializes the APGDAttack object with the given parameters.

        Args:
            predict: A callable representing the forward pass of the model.
            n_iter: Number of iterations for the attack.
            norm: The norm type for the attack ('Linf', 'L2', 'L1').
            n_restarts: Number of random restarts for the attack.
            eps: The maximum perturbation amount allowed.
            seed: Random seed for reproducibility.
            loss: Type of loss function to use.
            eot_iter: Number of iterations for Expectation over Transformation.
            rho: Parameter for adjusting step size.
            topk: Parameter for controlling sparsity in 'L1' norm.
            verbose: If True, enables verbose output.
            device: The device on which to perform computations.
            use_largereps: If True, uses larger epsilon values initially.
            is_tf_model: If True, indicates a TensorFlow model.
        """
        self.model = predict
        self.n_iter = n_iter
        self.eps = eps
        self.norm = norm
        self.n_restarts = n_restarts
        self.seed = seed
        self.loss = loss
        self.eot_iter = eot_iter
        self.thr_decr = rho
        self.topk = topk
        self.verbose = verbose
        self.device = device
        self.use_rs = True
        self.use_largereps = use_largereps
        self.n_iter_orig = n_iter + 0
        self.eps_orig = eps + 0.
        self.is_tf_model = is_tf_model
        self.y_target = None

    def init_hyperparam(self, x: torch.Tensor) -> None:
        """
        Initializes various hyperparameters based on the input data.

        Args:
            x (torch.Tensor): The input data.
        """
        assert self.norm in ['Linf', 'L2', 'L1']
        assert self.eps is not None
        if self.device is None:
            self.device = x.device
        self.orig_dim = list(x.shape[1:])
        self.ndims = len(self.orig_dim)
        if self.seed is None:
            self.seed = time.time()

        # set parameters for checkpoints
        self.n_iter_2 = max(int(0.22 * self.n_iter), 1)
        self.n_iter_min = max(int(0.06 * self.n_iter), 1)
        self.size_decr = max(int(0.03 * self.n_iter), 1)

    def check_oscillation(self, x: torch.Tensor, j: int, k: int, y5: torch.Tensor, k3: float = 0.75) -> torch.Tensor:
        """
        Checks for oscillation in the optimization process to adjust step sizes.

        Args:
            x (torch.Tensor): The input tensor.
            j (int): Current iteration index.
            k (int): The number of steps to look back for oscillation.
            y5 (torch.Tensor): The tensor of losses.
            k3 (float, optional): Threshold parameter for oscillation. Defaults to 0.75.

        Returns:
            torch.Tensor: Tensor indicating if oscillation is detected.
        """
        t = torch.zeros(x.shape[1]).to(self.device)
        for counter5 in range(k):
            t += (x[j - counter5] > x[j - counter5 - 1]).float()
        return (t <= k * k3 * torch.ones_like(t)).float()

    def check_shape(self, x: torch.Tensor) -> torch.Tensor:
        """
        Ensures the input tensor has the correct shape.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The reshaped tensor.
        """
        return x if len(x.shape) > 0 else x.unsqueeze(0)

    def normalize(self, x: torch.Tensor) -> torch.Tensor:
        """
        Normalizes the input tensor based on the specified norm type.

        Args:
            x (torch.Tensor): The input tensor to be normalized.

        Returns:
            torch.Tensor: The normalized tensor.
        """
        if self.norm == 'Linf':
            t = x.abs().view(x.shape[0], -1).max(1)[0]
            return x / (t.view(-1, *([1] * self.ndims)) + 1e-12)
        elif self.norm == 'L2':
            t = (x ** 2).view(x.shape[0], -1).sum(-1).sqrt()
            return x / (t.view(-1, *([1] * self.ndims)) + 1e-12)
        elif self.norm == 'L1':
            try:
                t = x.abs().view(x.shape[0], -1).sum(dim=-1)
            except RuntimeError:
                t = x.abs().reshape([x.shape[0], -1]).sum(dim=-1)
            return x / (t.view(-1, *([1] * self.ndims)) + 1e-12)

    def lp_norm(self, x: torch.Tensor) -> torch.Tensor:
        """
        Computes the Lp norm of the input tensor.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The computed Lp norm of the input tensor.
        """
        if self.norm == 'L2':
            t = (x ** 2).view(x.shape[0], -1).sum(-1).sqrt()
            return t.view(-1, *([1] * self.ndims))

    def dlr_loss(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        """
        Computes the Deep Learning Robustness (DLR) loss.

        Args:
            x (torch.Tensor): The logits from the model.
            y (torch.Tensor): The target labels.

        Returns:
            torch.Tensor: The computed DLR loss.
        """
        x_sorted, ind_sorted = x.sort(dim=1)
        ind = (ind_sorted[:, -1] == y).float()
        u = torch.arange(x.shape[0])
        return -(x[u, y] - x_sorted[:, -2] * ind - x_sorted[:, -1] * (
            1. - ind)) / (x_sorted[:, -1] - x_sorted[:, -3] + 1e-12)

    def attack_single_run(self, x: torch.Tensor,
                          y: torch.Tensor,
                          x_init: Optional[torch.Tensor] = None
                          ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Performs a single run of the attack.

        Args:
            x (torch.Tensor): The input data (clean images).
            y (torch.Tensor): The target labels.
            x_init (Optional[torch.Tensor]): Initial starting point for the attack.

        Returns:
            Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]: A tuple containing the best perturbed inputs,
            the accuracy tensor, the loss tensor, and the best adversarial examples found.
        """
        if len(x.shape) < self.ndims:
            x = x.unsqueeze(0)
            y = y.unsqueeze(0)
        if self.norm == 'Linf':
            t = 2 * torch.rand(x.shape).to(self.device).detach() - 1
            x_adv = x + self.eps * torch.ones_like(x).detach() * self.normalize(t)
        elif self.norm == 'L2':
            t = torch.randn(x.shape).to(self.device).detach()
            x_adv = x + self.eps * torch.ones_like(x).detach() * self.normalize(t)
        elif self.norm == 'L1':
            t = torch.randn(x.shape).to(self.device).detach()
            delta = L1_projection(x, t, self.eps)
            x_adv = x + t + delta
        if x_init is not None:
            x_adv = x_init.clone()
            if self.norm == 'L1' and self.verbose:
                print('[custom init] L1 perturbation {:.5f}'.format(
                    (x_adv - x).abs().view(x.shape[0], -1).sum(1).max()))
        x_adv = x_adv.clamp(0., 1.)
        x_best = x_adv.clone()
        x_best_adv = x_adv.clone()
        loss_steps = torch.zeros([self.n_iter, x.shape[0]]).to(self.device)
        loss_best_steps = torch.zeros([self.n_iter + 1, x.shape[0]]).to(self.device)
        acc_steps = torch.zeros_like(loss_best_steps)
        if not self.is_tf_model:
            if self.loss == 'ce':
                criterion_indiv = nn.CrossEntropyLoss(reduction='none')
            elif self.loss == 'ce-targeted-cfts':
                def criterion_indiv(x, y):
                    return -1. * F.cross_entropy(x, y, reduction='none')
            elif self.loss == 'dlr':
                criterion_indiv = self.dlr_loss
            elif self.loss == 'dlr-targeted':
                criterion_indiv = self.dlr_loss_targeted
            elif self.loss == 'ce-targeted':
                criterion_indiv = self.ce_loss_targeted
            else:
                raise ValueError('unknowkn loss')
        else:
            if self.loss == 'ce':
                criterion_indiv = self.model.get_logits_loss_grad_xent
            elif self.loss == 'dlr':
                criterion_indiv = self.model.get_logits_loss_grad_dlr
            elif self.loss == 'dlr-targeted':
                criterion_indiv = self.model.get_logits_loss_grad_target
            else:
                raise ValueError('unknowkn loss')

        x_adv.requires_grad_()
        grad = torch.zeros_like(x)
        for _ in range(self.eot_iter):
            if not self.is_tf_model:
                with torch.enable_grad():
                    logits = self.model(x_adv)
                    loss_indiv = criterion_indiv(logits, y)
                    loss = loss_indiv.sum()
                grad += torch.autograd.grad(loss, [x_adv])[0].detach()
            else:
                if self.y_target is None:
                    logits, loss_indiv, grad_curr = criterion_indiv(x_adv, y)
                else:
                    logits, loss_indiv, grad_curr = criterion_indiv(x_adv, y, self.y_target)
                grad += grad_curr

        grad /= float(self.eot_iter)
        grad_best = grad.clone()
        acc = logits.detach().max(1)[1] == y
        acc_steps[0] = acc + 0
        loss_best = loss_indiv.detach().clone()
        alpha = 2. if self.norm in ['Linf', 'L2'] else 1. if self.norm in ['L1'] else 2e-2
        step_size = alpha * self.eps * torch.ones([x.shape[0], *(
            [1] * self.ndims)]).to(self.device).detach()
        x_adv_old = x_adv.clone()
        k = self.n_iter_2 + 0
        if self.norm == 'L1':
            k = max(int(.04 * self.n_iter), 1)
            n_fts = math.prod(self.orig_dim)
            if x_init is None:
                topk = .2 * torch.ones([x.shape[0]], device=self.device)
                sp_old = n_fts * torch.ones_like(topk)
            else:
                topk = L0_norm(x_adv - x) / n_fts / 1.5
                sp_old = L0_norm(x_adv - x)

            adasp_redstep = 1.5
            adasp_minstep = 10.

        counter3 = 0
        loss_best_last_check = loss_best.clone()
        reduced_last_check = torch.ones_like(loss_best)
        # n_reduced = 0
        n_fts = x.shape[-3] * x.shape[-2] * x.shape[-1]
        u = torch.arange(x.shape[0], device=self.device)
        for i in range(self.n_iter):
            # gradient step
            with torch.no_grad():
                x_adv = x_adv.detach()
                grad2 = x_adv - x_adv_old
                x_adv_old = x_adv.clone()
                a = 0.75 if i > 0 else 1.0
                if self.norm == 'Linf':
                    x_adv_1 = x_adv + step_size * torch.sign(grad)
                    x_adv_1 = torch.clamp(torch.min(torch.max(x_adv_1, x - self.eps), x + self.eps), 0.0, 1.0)
                    x_adv_1 = torch.clamp(torch.min(torch.max(
                        x_adv + (x_adv_1 - x_adv) * a + grad2 * (1 - a),
                        x - self.eps), x + self.eps), 0.0, 1.0)
                elif self.norm == 'L2':
                    x_adv_1 = x_adv + step_size * self.normalize(grad)
                    x_adv_1 = torch.clamp(x + self.normalize(x_adv_1 - x) *
                                          torch.min(self.eps * torch.ones_like(x).detach(), self.lp_norm(x_adv_1 - x)),
                                          0.0, 1.0)
                    x_adv_1 = x_adv + (x_adv_1 - x_adv) * a + grad2 * (1 - a)
                    x_adv_1 = torch.clamp(
                        x + self.normalize(x_adv_1 - x)
                        * torch.min(
                            self.eps * torch.ones_like(x).detach(),
                            self.lp_norm(x_adv_1 - x)
                        ),
                        0.0,
                        1.0
                    )

                elif self.norm == 'L1':
                    grad_topk = grad.abs().view(x.shape[0], -1).sort(-1)[0]
                    topk_curr = torch.clamp((1. - topk) * n_fts, min=0, max=n_fts - 1).long()
                    grad_topk = grad_topk[u, topk_curr].view(-1, *[1] * (len(x.shape) - 1))
                    sparsegrad = grad * (grad.abs() >= grad_topk).float()
                    x_adv_1 = x_adv + step_size * sparsegrad.sign() / (sparsegrad.sign().abs().view(x.shape[0], -1)
                                                                       .sum(dim=-1).view(-1, *[1] * (len(x.shape) - 1))
                                                                       + 1e-10)
                    delta_u = x_adv_1 - x
                    delta_p = L1_projection(x, delta_u, self.eps)
                    x_adv_1 = x + delta_u + delta_p
                x_adv = x_adv_1 + 0.
            # get gradient
            x_adv.requires_grad_()
            grad = torch.zeros_like(x)
            for _ in range(self.eot_iter):
                if not self.is_tf_model:
                    with torch.enable_grad():
                        logits = self.model(x_adv)
                        loss_indiv = criterion_indiv(logits, y)
                        loss = loss_indiv.sum()

                    grad += torch.autograd.grad(loss, [x_adv])[0].detach()
                else:
                    if self.y_target is None:
                        logits, loss_indiv, grad_curr = criterion_indiv(x_adv, y)
                    else:
                        logits, loss_indiv, grad_curr = criterion_indiv(x_adv, y, self.y_target)
                    grad += grad_curr

            grad /= float(self.eot_iter)
            pred = logits.detach().max(1)[1] == y
            acc = torch.min(acc, pred)
            acc_steps[i + 1] = acc + 0
            ind_pred = (pred == 0).nonzero().squeeze()
            x_best_adv[ind_pred] = x_adv[ind_pred] + 0.
            if self.verbose:
                str_stats = ' - step size: {:.5f} - topk: {:.2f}'.format(
                    step_size.mean(), topk.mean() * n_fts) if self.norm in ['L1'] else ''
                print('[m] iteration: {} - best loss: {:.6f} - robust accuracy: {:.2%}{}'.format(
                    i, loss_best.sum(), acc.float().mean(), str_stats))

            # check step size
            with torch.no_grad():
                y1 = loss_indiv.detach().clone()
                loss_steps[i] = y1 + 0
                ind = (y1 > loss_best).nonzero().squeeze()
                x_best[ind] = x_adv[ind].clone()
                grad_best[ind] = grad[ind].clone()
                loss_best[ind] = y1[ind] + 0
                loss_best_steps[i + 1] = loss_best + 0
                counter3 += 1
                if counter3 == k:
                    if self.norm in ['Linf', 'L2']:
                        fl_oscillation = self.check_oscillation(loss_steps, i, k, loss_best, k3=self.thr_decr)
                        fl_reduce_no_impr = (1. - reduced_last_check) * (
                            loss_best_last_check >= loss_best).float()
                        fl_oscillation = torch.max(fl_oscillation, fl_reduce_no_impr)
                        reduced_last_check = fl_oscillation.clone()
                        loss_best_last_check = loss_best.clone()

                        if fl_oscillation.sum() > 0:
                            ind_fl_osc = (fl_oscillation > 0).nonzero().squeeze()
                            step_size[ind_fl_osc] /= 2.0
                            # n_reduced = fl_oscillation.sum()

                            x_adv[ind_fl_osc] = x_best[ind_fl_osc].clone()
                            grad[ind_fl_osc] = grad_best[ind_fl_osc].clone()
                        k = max(k - self.size_decr, self.n_iter_min)

                    elif self.norm == 'L1':
                        sp_curr = L0_norm(x_best - x)
                        fl_redtopk = (sp_curr / sp_old) < .95
                        topk = sp_curr / n_fts / 1.5
                        step_size[fl_redtopk] = alpha * self.eps
                        step_size[~fl_redtopk] /= adasp_redstep
                        step_size.clamp_(alpha * self.eps / adasp_minstep, alpha * self.eps)
                        sp_old = sp_curr.clone()

                        x_adv[fl_redtopk] = x_best[fl_redtopk].clone()
                        grad[fl_redtopk] = grad_best[fl_redtopk].clone()

                    counter3 = 0

        return (x_best, acc, loss_best, x_best_adv)

    def perturb(self, x: torch.Tensor, y: Optional[torch.Tensor] = None,
                best_loss: bool = False, x_init: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Generates adversarial examples for the given inputs.

        Args:
            x (torch.Tensor): Clean images.
            y (Optional[torch.Tensor]): Clean labels. If None, predicted labels are used.
            best_loss (bool, optional): If True, returns points with highest loss. Defaults to False.
            x_init (Optional[torch.Tensor]): Initial starting point for the attack.

        Returns:
            torch.Tensor: Adversarial examples.
        """
        assert self.loss in ['ce', 'dlr']
        if y is not None and len(y.shape) == 0:
            x.unsqueeze_(0)
            y.unsqueeze_(0)
        self.init_hyperparam(x)
        x = x.detach().clone().float().to(self.device)
        if not self.is_tf_model:
            y_pred = self.model(x).max(1)[1]
        else:
            y_pred = self.model.predict(x).max(1)[1]
        if y is None:
            y = y_pred.detach().clone().long().to(self.device)
        else:
            y = y.detach().clone().long().to(self.device)
        adv = x.clone()
        if self.loss != 'ce-targeted':
            acc = y_pred == y
        else:
            acc = y_pred != y
        # loss = -1e10 * torch.ones_like(acc).float()
        if self.verbose:
            print('-------------------------- ', 'running {}-attack with epsilon {:.5f}'.format(self.norm, self.eps),
                  '--------------------------')
            print('initial accuracy: {:.2%}'.format(acc.float().mean()))

        if self.use_largereps:
            epss = [3. * self.eps_orig, 2. * self.eps_orig, 1. * self.eps_orig]
            iters = [.3 * self.n_iter_orig, .3 * self.n_iter_orig, .4 * self.n_iter_orig]
            iters = [math.ceil(c) for c in iters]
            iters[-1] = self.n_iter_orig - sum(iters[:-1])  # make sure to use the given iterations
            if self.verbose:
                print('using schedule [{}x{}]'.format('+'.join([str(c) for c in epss]),
                                                      '+'.join([str(c) for c in iters])))

        startt = time.time()
        if not best_loss:
            torch.random.manual_seed(self.seed)
            torch.cuda.random.manual_seed(self.seed)
            for counter in range(self.n_restarts):
                ind_to_fool = acc.nonzero().squeeze()
                if len(ind_to_fool.shape) == 0:
                    ind_to_fool = ind_to_fool.unsqueeze(0)
                if ind_to_fool.numel() != 0:
                    x_to_fool = x[ind_to_fool].clone()
                    y_to_fool = y[ind_to_fool].clone()

                    if not self.use_largereps:
                        res_curr = self.attack_single_run(x_to_fool, y_to_fool)
                    else:
                        res_curr = self.decr_eps_pgd(x_to_fool, y_to_fool, epss, iters)
                    best_curr, acc_curr, loss_curr, adv_curr = res_curr
                    ind_curr = (acc_curr == 0).nonzero().squeeze()
                    acc[ind_to_fool[ind_curr]] = 0
                    adv[ind_to_fool[ind_curr]] = adv_curr[ind_curr].clone()
                    if self.verbose:
                        print('restart {} - robust accuracy: {:.2%}'.format(
                            counter, acc.float().mean()),
                            '- cum. time: {:.1f} s'.format(
                            time.time() - startt))
            return adv.detach().clone()
        else:
            adv_best = x.detach().clone()
            loss_best = torch.ones([x.shape[0]]).to(
                self.device) * (-float('inf'))
            for counter in range(self.n_restarts):
                best_curr, _, loss_curr, _ = self.attack_single_run(x, y)
                ind_curr = (loss_curr > loss_best).nonzero().squeeze()
                adv_best[ind_curr] = best_curr[ind_curr] + 0.
                loss_best[ind_curr] = loss_curr[ind_curr] + 0.
                if self.verbose:
                    print('restart {} - loss: {:.5f}'.format(counter, loss_best.sum()))
            return adv_best

    def decr_eps_pgd(self, x: torch.Tensor, y: torch.Tensor, epss: list, iters: list, use_rs: bool = True
                     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Performs PGD with decreasing epsilon values.

        Args:
            x (torch.Tensor): The input data.
            y (torch.Tensor): The target labels.
            epss (list): List of epsilon values to use in the attack.
            iters (list): List of iteration counts corresponding to each epsilon value.
            use_rs (bool, optional): If True, uses random start. Defaults to True.

        Returns:
            Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]: A tuple containing the final perturbed
            inputs, the accuracy tensor, the loss tensor, and the best adversarial examples found.
        """
        assert len(epss) == len(iters)
        assert self.norm in ['L1']
        self.use_rs = False
        if not use_rs:
            x_init = None
        else:
            x_init = x + torch.randn_like(x)
            x_init += L1_projection(x, x_init - x, 1. * float(epss[0]))
        # eps_target = float(epss[-1])
        if self.verbose:
            print('total iter: {}'.format(sum(iters)))
        for eps, niter in zip(epss, iters):
            if self.verbose:
                print('using eps: {:.2f}'.format(eps))
            self.n_iter = niter + 0
            self.eps = eps + 0.
            #
            if x_init is not None:
                x_init += L1_projection(x, x_init - x, 1. * eps)
            x_init, acc, loss, x_adv = self.attack_single_run(x, y, x_init=x_init)
        return (x_init, acc, loss, x_adv)
