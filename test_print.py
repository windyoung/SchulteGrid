# coding=utf-8
#!/usr/bin/env python3

import win32print
import win32ui
import win32con
import string

def print2Printer(self):
    # https://blog.csdn.net/ssshen14/article/details/77771181
    # http://timgolden.me.uk/pywin32-docs/win32print.html
    INCH = 1440

    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
    hDC.StartDoc ("Test doc")
    hDC.StartPage ()
    hDC.SetMapMode (win32con.MM_TWIPS)
    hDC.DrawText ("TEST HELLO  WORLD! CORSS FIREWALL, WE TOUCH THE WORLD!",
                    (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
    hDC.EndPage ()
    hDC.EndDoc ()


def p_string():
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)


    # string.ascii_letters
p_string()