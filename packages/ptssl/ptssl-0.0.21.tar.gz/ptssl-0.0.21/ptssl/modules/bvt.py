"""
BVT Basic Vulnerability Test – checks if any vulnerability exist.
Analyses the BVT item of a testssl JSON report to tell
whether if any vulnerability exist.

Contains:
- BVT class for performing the detection test.
- run() function as an entry point for running the test.

Usage:
    run(args, ptjsonlib)
"""

from ptlibs import ptjsonlib
from ptlibs.ptprinthelper import ptprint

__TESTLABEL__ = "Testing common vulnerabilities:"


class BVT:
    """
    BVT checks for basic vulnerabilities.

    It consumes the JSON output from testssl and check for basic vulnerabilities.
    """
    VULN_SEC_LEN = 21
    ERROR_NUM = -1

    def __init__(self, args: object, ptjsonlib: object, helpers: object, testssl_result: dict) -> None:
        self.args = args
        self.ptjsonlib = ptjsonlib
        self.helpers = helpers
        self.testssl_result = testssl_result

    def _find_section_bv(self) -> int:
        """
        Runs through JSON file and finds strat of cipher section.
        """
        id_number = 0
        for item in self.testssl_result:
            if item["id"] == "heartbleed":
                return id_number
            id_number += 1
        return self.ERROR_NUM

    def _print_test_result(self) -> None:
        """
        Finds starting id of vulnerability section.
        Goes through the section and prints out vulnerabilities.
        1) OK
        2) INFO - prints warning information
        3) VULN - prints out vulnerabilities
        """
        id_section = self._find_section_bv()
        if id_section == self.ERROR_NUM:
            self.ptjsonlib.end_error("testssl could not provide vulnerability section", self.args.json)
            return

        for item in self.testssl_result[id_section:id_section + self.VULN_SEC_LEN]:
            if item["id"] == "DROWN_hint" or item["id"] == "LOGJAM-common_primes":
                continue
            if item["severity"] == "OK":
                if item["id"] == "fallback_SCSV" or item["id"] == "secure_renego":
                    ptprint(f"{item["id"]:<23}  supported", "OK", not self.args.json, indent=4)
                else:
                    ptprint(f"{item["id"]:<23}  not vulnerable", "OK", not self.args.json, indent=4)
            elif item["severity"] == "INFO":
                ptprint(f"{item["id"]:<23}  {item["finding"]}", "WARNING", not self.args.json, indent=4)
                self.ptjsonlib.add_vulnerability(
                    f'PTV-WEB-MISC-{''.join(ch for ch in item["id"] if ch.isalnum()).upper()}')
            else:
                if item["id"] == "fallback_SCSV" or item["id"] == "secure_renego":
                    ptprint(f"{item["id"]:<23}  not supported", "VULN", not self.args.json, indent=4)
                else:
                    ptprint(f"{item["id"]:<23}  vulnerable", "VULN", not self.args.json, indent=4)
                self.ptjsonlib.add_vulnerability(
                    f'PTV-WEB-MISC-{''.join(ch for ch in item["id"] if ch.isalnum()).upper()}')
        return


    def run(self) -> None:
        """
        Prints out the test label
        Execute the testssl report function.
        """
        ptprint(__TESTLABEL__, "TITLE", not self.args.json, colortext=True)
        self._print_test_result()
        return


def run(args, ptjsonlib, helpers, testssl_result):
    """Entry point for running the BVT module (Basic Vulnerability Test)."""
    BVT(args, ptjsonlib, helpers, testssl_result).run()