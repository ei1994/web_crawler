#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
写入和读取基本方法练习
"""

from xml.dom import minidom

#写入xml文档的方法
def create_xml_test(filename):
    #新建xml文档对象
    xml=minidom.Document()
    
    #创建第一个节点，第一个节点就是根节点了
    root=xml.createElement('root')
    
    #写入属性（xmlns:xsi是命名空间，同样还可以写入xsi:schemaLocation指定xsd文件）
    root.setAttribute('xmlns:xsi',"http://www.w3.org")
    
    #创建节点后，还需要添加到文档中才有效
    xml.appendChild(root)
    
    #一般根节点是很少写文本内容，那么给根节点再创建一个子节点
    text_node=xml.createElement('element')
    text_node.setAttribute('id','id1')
    root.appendChild(text_node)
    
    #给这个节点加入文本，文本也是一种节点
    text=xml.createTextNode('hello world')
    text_node.appendChild(text)
    
    #一个节点加了文本之后，还可以继续追加其他东西
    tag=xml.createElement('tag')
    tag.setAttribute('data','tag data')
    text_node.appendChild(tag)
    
    #写好之后，就需要保存文档了
    f=open(filename,'wb')
    f.write(xml.toprettyxml(encoding='utf-8'))
    f.close()

#读取xml文档的方法
def read_xml_test(filename):
    #打开这个文档，用parse方法解析
    xml=minidom.parse(filename)
    
    #获取根节点
    root=xml.documentElement
    
    #得到根节点下面所有的element节点
    #更多方法可以参考w2school的内容或者用dir(root)获取
    elements=root.getElementsByTagName('element')
    
    #遍历处理，elements是一个列表
    for element in elements:
        #判断是否有id属性
        if element.hasAttribute('id'):
            #不加上面的判断也可以，若找不到属性，则返回空
            print ('id:',element.getAttribute('id'))
        
        #遍历element的子节点
        for node in element.childNodes:
            #通过nodeName判断是否是文本
            if node.nodeName=='#text':
                #用data属性获取文本内容
                text = node.data.replace('\n','')
                #这里的文本需要特殊处理一下，会有多余的'\n'
                print( u'\t文本：',text)
            else:
                #输出节点名
                print ('\t'+node.nodeName)
 
                #输出属性值，这里可以用getAttribute方法获取
                #也可以遍历得到，这是一个字典
                for attr,attr_val in node.attributes.items():
                    print( '\t\t',attr,':',attr_val)
        print( '')
 
if __name__ == '__main__':
    #在当前目录下，创建1.xml
    create_xml_test('2.xml')
    read_xml_test('2.xml')
 

  
  
    
    
    