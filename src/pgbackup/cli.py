from argparse import ArgumentParser,Action

known_drivers = ['local','s3']
class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local'\
                         and 'S3'")
        namespace.driver = driver.lower()
        namespace.destination = destination



def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url',help="URL of the PostgreSQL database to backup")
    parser.add_argument('--driver',
                        help="How and where to store the backup",
                        nargs=2,
                        action=DriverAction,
                        required=True)
    return parser

