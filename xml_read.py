
'''
读取 xml 文件
'''
from xml.dom import minidom

def read_xml_test(filename):
    #打开这个文档，用parse方法解析
    xml=minidom.parse(filename)
    
    #获取根节点
    root=xml.documentElement
    
    #得到根节点下面所有的book节点
    #更多方法可以参考w2school的内容或者用dir(root)获取
    book=root.getElementsByTagName('book')
    
    #遍历处理，elements是一个列表
    for book in book:
        #判断是否有id属性
        if book.hasAttribute('genre'):
            #不加上面的判断也可以，若找不到属性，则返回空
            print ('genre:',book.getAttribute('genre'))
        
        #遍历element的子节点
        for node in book.childNodes:
#            print('a', book.getElementsByTagName('title'))
#            print(node.firstChild.data)
#            #通过nodeName判断是否是文本
            if node.nodeName=='#text':
##                用data属性获取文本内容
##                text = node.data.replace('\n','')
##                这里的文本需要特殊处理一下，会有多余的'\n'
##                print( u'\t文本：',text)
##                print ('\t'+node.nodeName)
                pass
            else:
                
#                #输出节点名
                print (' '+node.nodeName+':')
                print(node.firstChild.data)
                print (str(node.childNodes))

if __name__ == '__main__':
    read_xml_test('bookstore.xml')
  