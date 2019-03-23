#! env python
# -*- coding: utf-8 -*-

import os
import sys

# Date: 2019/03/23
# Filename: xml_sample

import xml.etree.ElementTree as ET

__author__ = 'yoshiaki'
__date__ = "2019/03/23"

def main():
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

    # ---------- 書き込み----------------
    root = ET.Element("root")

    employee = ET.SubElement(root, "employee")
    employ = ET.SubElement(employee, "employ")

    # 属性の追加
    employ_id = ET.SubElement(employ, "id", {'Attribute1': "@@@"})
    employ_id.text = "111"

    employ_name = ET.SubElement(employ, "name")
    employ_name.text = "Mike"

    # ファイルに出力
    tree = ET.ElementTree(element=root)
    tree.write("test2.xml", encoding="utf-8", xml_declaration=True)

    # ------------------出力--------------------------------
    tree = ET.ElementTree(file="test2.xml")
    root = tree.getroot()

    for employee in root:
        for employ in employee:
            for person in employ:
                print(person.tag, person.text)

    # 出力部分を抽出する場合
    print(root[0][0][0].text)
    print(root[0][0][0].attrib.get("Attribute1"))

    return


if __name__ == '__main__':
    main()
