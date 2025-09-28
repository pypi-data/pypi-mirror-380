import sys

import ut_com.dec as dec

from ut_com.com import Com 
from ap_mail.parms import Parms
from ap_mail.task import Task


class Do:

    @classmethod
    @dec.handle_error
    @dec.timer
    def do(cls) -> None:
        Task.do(Com.sh_kwargs(cls, Parms, sys.argv))


if __name__ == "__main__":
    Do.do()
