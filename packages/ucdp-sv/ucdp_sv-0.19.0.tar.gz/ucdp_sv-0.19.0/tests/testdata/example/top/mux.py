#
# MIT License
#
# Copyright (c) 2024-2025 nbiotcloud
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Example."""

import ucdp as u
from fileliststandard import HdlFileList


class MyEnumType(u.AEnumType):
    """Just My Enumeration."""

    keytype: u.ClassVar[u.UintType] = u.UintType(3)

    def _build(self):
        self._add(0, "one")
        self._add(1, "two")
        self._add(2, "three")


class MuxMod(u.AMod):
    """Module using Multiplexer."""

    filelists: u.ClassVar[u.ModFileLists] = (HdlFileList(gen="full"),)

    def _build(self):
        sel = self.add_signal(u.UintType(3), "sel_s")
        self.add_port(u.UintType(4), "a0_i")
        b0 = self.add_port(u.UintType(4), "b0_i")
        self.add_port(u.UintType(4), "c0_i")
        q0 = self.add_port(u.UintType(4), "q0_o")

        self.add_port(MyEnumType(), "sel_i")

        self.add_port(u.UintType(8), "a1_i")
        self.add_port(u.UintType(8), "b1_i")
        self.add_port(u.UintType(8), "c1_i")
        self.add_port(u.UintType(8), "q1_o")

        self.add_port(u.UintType(8), "q2_o")

        self.add_signal(u.UintType(4), "q3_s")

        self.add_port(u.UintType(4), "q4_o")

        self.add_type_consts(MyEnumType())

        mux = self.add_mux("main", title="title", descr="descr", comment="comment")

        mux.set_default("q0_o", u.UintType(4, default=8))
        mux.set("sel_s", "3h1", "q0_o", "a0_i")
        mux.set(sel, "3h2", q0, b0)
        mux.set(sel, "3h4", q0, "c0_i")

        mux.set(sel, "3h4", "q3_s", "c0_i")

        mux.set("sel_i", "my_enum_two_e", "q4_o", "b0_i")
        mux.set("sel_i", self.ports["sel_i"].type_.new(default=3), "q4_o", "a0_i")

        mux.set("sel_s", "3h0", "q1_o", "a1_i")
        mux.set("sel_s", "3h1", "q1_o", "b1_i")
        mux.set_default("q1_o", "c1_i")

        mux = self.add_mux("slim")
        mux.set("sel_s", "3h1", "q2_o", "a1_i")

        mux = self.add_mux("empty")
