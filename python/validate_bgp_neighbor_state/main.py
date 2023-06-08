# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.dp import Action


# ---------------
# ACTIONS EXAMPLE
# ---------------
class DoubleAction(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info('action name: ', name)
        self.log.info('action input.device: ', input.device)
        self.log.info('action input.bgp_neighbor_addr: ', input.bgp_neighbor_addr)
        node_path = f"/ncs:devices/device{{{input.device}}}/live-status/ios-stats:bgp/ipv4/unicast/neighbors{{{input.bgp_neighbor_addr}}}/ios-stats:bgp-state"
        self.log.info('node_path: ', node_path)
        result = ncs.maagic.get_node(trans, node_path)
        self.log.info('bgp state result: ', result)
        # Set the output which is returned with Action is run.
        output.bgp_state = result

# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        self.log.info('Main RUNNING')
        self.register_action('validate-bgp-neighbor-state-action', DoubleAction)

    def teardown(self):
        self.log.info('Main FINISHED')
