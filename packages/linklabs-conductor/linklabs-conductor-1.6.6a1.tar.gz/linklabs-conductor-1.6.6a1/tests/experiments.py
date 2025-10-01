import coloredlogs
import logging

import conductor.airfinder as af

READ_SITE_INFO = False
TEST_ASSET_GROUPS = False
MODIFY_SITE_INFO = False
ALERT_TAG_TESTING = True
WEB_SOCKET = False


def main():
    coloredlogs.install(level='DEBUG')
    logger = logging.getLogger(__name__)

    #a = conductor.ConductorAccount('thomas.steinholz@link-labs.com')
    u = af.User('thomas.steinholz@link-labs.com')

    ############################################################################
    # Websocket Testing
    ############################################################################
    if WEB_SOCKET:
        APP_TOKEN_S = '20028716136f69533e19'
        app_token = u.get_application_token(APP_TOKEN_S)

        def sub_callback(msg):
            logger.info(msg)

        logger.info("Starting the subscription...")
        sub = app_token.subscribe(sub_callback)
        #asyncio.run(sub.connect())

        logger.info("Waiting for events...")

        try:
            sub.connect_and_wait()
        except:
            sub.close()
            logger.warning("Sub has been closed")

    ############################################################################
    # Alert Tag Testing
    ############################################################################
    if ALERT_TAG_TESTING:
        tag = u.get_device("F9286E1EAABF")
        logger.info("{} {} {}".format(tag, tag.subject_id, tag.subject_mac))
        #tag.send_alert_ack()
        #tag.send_alert_close()


    ############################################################################
    # Reading Site information
    ############################################################################
    if READ_SITE_INFO:
        sites = u.get_sites()
        site = None
        for s in sites:
            if 'cardinal' in s.name.lower():
                site = s
                break

        if not site:
            print("No site found!")
            return

        print("Site: {}\n".format(site.name))

        print("SiteUsers:")
        for user in site.get_site_users():
            print("\t{}".format(user.name))
        print('-----------------------------------------\n')

        for area in site.get_areas():
            print("\tArea: {}".format(area.name))

            for zone in area.get_zones():
                print("\t\tZone: {}".format(zone.name))

                for loc in zone.get_locations():
                    print("\t\t\tLocation: {}".format(loc))
                print()
            print('-----------------------------------------\n')


    ############################################################################
    # Airfinder Modififcation
    ############################################################################
    if MODIFY_SITE_INFO:

        # Make a Site
        site = u.create_site('test site 1')

        # Make 2 Areas


        # Rename one zone
        zone2.rename("TestZone2")

        print(site.get_zones())

        # Make 3 Zones in each area
        zone1 = site.create_zone("test zone 1")
        zone2 = site.create_zone("test zone 2")

        print(zone1)
        print(zone2)
        # Rename a zone

        # Add tags

        # Remove tags

        # Delete Everything

    ############################################################################
    # Asset Group Testing
    ############################################################################
    if TEST_ASSET_GROUPS:
        #asset_group = a.create_asset_group("testing group") # Works!
        asset_groups = a.get_asset_groups() #-- Works
        print(asset_groups) #-- Works
        asset_group = asset_groups[0] #-- Works
        #print(asset_group.get_metadata()) # -- Does NOT Work!

        #print(asset_group._data) # DEBUG

    #    print(asset_group.add_node('$501$0-0-0000de5-faf383555'))
        #asset_group.add_node('$501$0-0-0000C53-6D785B13B')      # Works!
        #asset_group.remove_node('$501$0-0-0000C53-6D785B13B')   # Works!
        #nodes = asset_group.get_nodes() #-- Works
        print(nodes[-1].get_asset_groups()[0].get_nodes()) #-- Works
        #print(nodes[-1].get_asset_groups()[0].get_application_tokens()) #-- Doesn't Works
        #print(asset_group.name)
        #asset_group.rename("Test Group") # Works
        print(asset_group.name) #-- Works

    #    print(asset_group.send_message('DEADBEEF')) -- Not Possible



main()
