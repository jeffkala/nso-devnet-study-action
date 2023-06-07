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
        query = trans.get_oper()
        # Specify the XPath to retrieve BGP neighbor status
        query.xpath(f'/devices/device[name="{input.device}"]/live-status/bgp/neighbor')

        # Execute the query and retrieve the result
        result = query.apply()
        self.log.info('result: ', result)

# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        self.log.info('Main RUNNING')
        self.register_action('validate-bgp-neighbor-state-action', DoubleAction)

    def teardown(self):
        self.log.info('Main FINISHED')
