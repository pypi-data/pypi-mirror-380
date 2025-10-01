"""Module for the Interaction Network block."""

import torch
from torch_geometric.nn import MessagePassing
from ....utils import check_positive_integer
from ....model import FeedForward


class InteractionNetworkBlock(MessagePassing):
    """
    Implementation of the Interaction Network block.

    This block is used to perform message-passing between nodes and edges in a
    graph neural network, following the scheme proposed by Battaglia et al. in
    2016. It serves as an inner block in a larger graph neural network
    architecture.

    The message between two nodes connected by an edge is computed by applying a
    multi-layer perceptron (MLP) to the concatenation of the sender and
    recipient node features. Messages are then aggregated using an aggregation
    scheme (e.g., sum, mean, min, max, or product).

    The update step is performed by applying another MLP to the concatenation of
    the incoming messages and the node features.

    .. seealso::

        **Original reference**: Battaglia, P. W., et al. (2016).
        *Interaction Networks for Learning about Objects, Relations and
        Physics*.
        In Advances in Neural Information Processing Systems (NeurIPS 2016).
        DOI: `<https://doi.org/10.48550/arXiv.1612.00222>`_.
    """

    def __init__(
        self,
        node_feature_dim,
        edge_feature_dim=0,
        hidden_dim=64,
        n_message_layers=2,
        n_update_layers=2,
        activation=torch.nn.SiLU,
        aggr="add",
        node_dim=-2,
        flow="source_to_target",
    ):
        """
        Initialization of the :class:`InteractionNetworkBlock` class.

        :param int node_feature_dim: The dimension of the node features.
        :param int edge_feature_dim: The dimension of the edge features.
            If edge_attr is not provided, it is assumed to be 0.
            Default is 0.
        :param int hidden_dim: The dimension of the hidden features.
            Default is 64.
        :param int n_message_layers: The number of layers in the message
            network. Default is 2.
        :param int n_update_layers: The number of layers in the update network.
            Default is 2.
        :param torch.nn.Module activation: The activation function.
            Default is :class:`torch.nn.SiLU`.
        :param str aggr: The aggregation scheme to use for message passing.
            Available options are "add", "mean", "min", "max", "mul".
            See :class:`torch_geometric.nn.MessagePassing` for more details.
            Default is "add".
        :param int node_dim: The axis along which to propagate. Default is -2.
        :param str flow: The direction of message passing. Available options
            are "source_to_target" and "target_to_source".
            The "source_to_target" flow means that messages are sent from
            the source node to the target node, while the "target_to_source"
            flow means that messages are sent from the target node to the
            source node. See :class:`torch_geometric.nn.MessagePassing` for more
            details. Default is "source_to_target".
        :raises AssertionError: If `node_feature_dim` is not a positive integer.
        :raises AssertionError: If `hidden_dim` is not a positive integer.
        :raises AssertionError: If `n_message_layers` is not a positive integer.
        :raises AssertionError: If `n_update_layers` is not a positive integer.
        :raises AssertionError: If `edge_feature_dim` is not a non-negative
            integer.
        """
        super().__init__(aggr=aggr, node_dim=node_dim, flow=flow)

        # Check values
        check_positive_integer(node_feature_dim, strict=True)
        check_positive_integer(hidden_dim, strict=True)
        check_positive_integer(n_message_layers, strict=True)
        check_positive_integer(n_update_layers, strict=True)
        check_positive_integer(edge_feature_dim, strict=False)

        # Message network
        self.message_net = FeedForward(
            input_dimensions=2 * node_feature_dim + edge_feature_dim,
            output_dimensions=hidden_dim,
            inner_size=hidden_dim,
            n_layers=n_message_layers,
            func=activation,
        )

        # Update network
        self.update_net = FeedForward(
            input_dimensions=node_feature_dim + hidden_dim,
            output_dimensions=node_feature_dim,
            inner_size=hidden_dim,
            n_layers=n_update_layers,
            func=activation,
        )

    def forward(self, x, edge_index, edge_attr=None):
        """
        Forward pass of the block, triggering the message-passing routine.

        :param x: The node features.
        :type x: torch.Tensor | LabelTensor
        :param torch.Tensor edge_index: The edge indeces.
        :param edge_attr: The edge attributes. Default is None.
        :type edge_attr: torch.Tensor | LabelTensor
        :return: The updated node features.
        :rtype: torch.Tensor
        """
        return self.propagate(edge_index=edge_index, x=x, edge_attr=edge_attr)

    def message(self, x_i, x_j, edge_attr):
        """
        Compute the message to be passed between nodes and edges.

        :param x_i: The node features of the recipient nodes.
        :type x_i: torch.Tensor | LabelTensor
        :param x_j: The node features of the sender nodes.
        :type x_j: torch.Tensor | LabelTensor
        :return: The message to be passed.
        :rtype: torch.Tensor
        """
        if edge_attr is None:
            input_ = torch.cat((x_i, x_j), dim=-1)
        else:
            input_ = torch.cat((x_i, x_j, edge_attr), dim=-1)
        return self.message_net(input_)

    def update(self, message, x):
        """
        Update the node features with the received messages.

        :param torch.Tensor message: The message to be passed.
        :param x: The node features.
        :type x: torch.Tensor | LabelTensor
        :return: The updated node features.
        :rtype: torch.Tensor
        """
        return self.update_net(torch.cat((x, message), dim=-1))
