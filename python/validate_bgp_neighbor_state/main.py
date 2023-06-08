# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.dp import Action


# ---------------
# ACTIONS EXAMPLE
# ---------------
class DoubleAction(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):

        # EXAMPLE FROM SHELL
        # with ncs.maapi.Maapi() as m:
        #     with ncs.maapi.Session(m, 'admin', 'admin'):
        #         with m.start_write_trans(ncs.RUNNING) as t:
        #             node = ncs.maagic.get_node(t, '/ncs:devices/device{router-01}/live-status/ios-stats:bgp/ipv4/unicast/neighbors{1.1.1.2}/ios-stats:bgp-state')
        #             print(node)

        self.log.info('action name: ', name)
        self.log.info('action input.device: ', input.device)
        self.log.info('action input.bgp_neighbor_addr: ', input.bgp_neighbor_addr)
        root = ncs.maagic.get_root(trans)
        device = root.devices.device[input.device]
        result = ncs.maagic.get_node(trans,'/ncs:devices/device{router-01}/live-status/ios-stats:bgp/ipv4/unicast/neighbors{1.1.1.2}/ios-stats:bgp-state')
        self.log.info('result dir : ', dir(result))
        self.log.info('result: ', result)
        # Specify the XPath to retrieve BGP neighbor status
        # query.xpath(f'/devices/device[name="{input.device}"]/live-status/bgp/neighbor')

        # # Execute the query and retrieve the result
        # result = query.apply()
        # self.log.info('result: ', result)

# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        self.log.info('Main RUNNING')
        self.register_action('validate-bgp-neighbor-state-action', DoubleAction)

    def teardown(self):
        self.log.info('Main FINISHED')
