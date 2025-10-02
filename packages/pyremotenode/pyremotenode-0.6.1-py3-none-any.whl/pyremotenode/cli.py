import argparse
import logging
import os
import traceback

from pyremotenode.receiver.certus import JSONDataReceiver, DataReceiverHandler
from pyremotenode.schedule import Scheduler
from pyremotenode.utils import Configuration, setup_logging
from pyremotenode.utils.system import background_fork


def remotenode_main():
    # Don't use anything here that initiates the logging root handler
    a = argparse.ArgumentParser(usage="""
        If you're trying to run for debugging / coding

        try...

        run_pyremotenode -l logs/ -n -np -v configurations/certus.test.cfg

        or somesuch! Ctrl-C will kill the scheduler. Good luck! 
    """)
    a.add_argument("config", help="Configuration to use for running remote node")
    # TODO: Naming of service as a parameter...
    a.add_argument("--log-dir", "-l", help="Log directory",
                   default=os.path.join(os.sep,
                                        "data",
                                        "pyremotenode",
                                        "logs"))
    a.add_argument("--start-when-fail", "-s",
                   help="Start even if initial monitor checks fail",
                   action="store_true", default=False)
    a.add_argument("--pidfile", "-p",
                   help="PID file to manage for service operations",
                   default=os.path.join(os.sep,
                                        "var",
                                        "run",
                                        "{0}.pid".format(__name__)))
    a.add_argument("--no-pidfile", "-np", help="Don't check or create PID file",
                   default=False, action="store_true")
    a.add_argument("--no-daemon", "-n", help="Do not daemon",
                   default=False, action="store_true")
    a.add_argument("--verbose", "-v", help="Debugging information",
                   default=False, action="store_true")
    args = a.parse_args()

    if not args.no_daemon:
        background_fork()

    setup_logging("{}".format(os.path.basename(args.config)),
                  logdir=args.log_dir,
                  verbose=args.verbose)

    Configuration.check_file(args.config)
    cfg = Configuration(args.config).config

    try:
        pidfile = args.pidfile if not args.no_pidfile else None
        m = Scheduler(cfg,
                      start_when_fail=args.start_when_fail,
                      pid_file=pidfile)
        m.run()
    except Exception:
        # Last opportunity to log errors
        logging.error(traceback.format_exc())


def receiver_main():
    a = argparse.ArgumentParser()
    a.add_argument("-d", "--debug",
                   help="Write a transaction log",
                   action="store_true",
                   default=False)
    a.add_argument("--log-dir", "-l",
                   help="Log directory",
                   default="logs")
    a.add_argument("--pidfile", "-p",
                   help="PID file to manage for service operations",
                   default=os.path.join(os.sep,
                                        "var",
                                        "run",
                                        "{0}.pid".format(__name__)))
    a.add_argument("--no-pidfile", "-np", help="Don't check or create PID file",
                   default=False, action="store_true")
    a.add_argument("--no-daemon", "-n", help="Do not daemon",
                   default=False, action="store_true")
    a.add_argument("--verbose", "-v", help="Debugging information",
                   default=False, action="store_true")
    a.add_argument("--host-server", "-s", type=str, default="0.0.0.0")
    a.add_argument("port", help="TCP port to listen on", type=int)
    a.add_argument("directory", help="Output directory")
    args = a.parse_args()

    if not args.no_daemon:
        background_fork()

    setup_logging("{}".format("receiver.{}".format(args.port)),
                  logdir=args.log_dir,
                  verbose=args.verbose)
    ss = JSONDataReceiver((args.host_server, args.port),
                          DataReceiverHandler,
                          args.directory)
    logging.info("Starting server")
    ss.serve_forever()
    logging.info("Stopped listening for data...")

