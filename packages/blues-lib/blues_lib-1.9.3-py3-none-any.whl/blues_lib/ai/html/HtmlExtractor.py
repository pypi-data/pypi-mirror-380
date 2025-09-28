import re
import re
from bs4 import BeautifulSoup, Comment
import tiktoken

class HtmlExtractor:
  
  def extract(self,html:str)->dict[str,str|int]:
    """
    提取html的body有效内容并移除非必要属性
    这是唯一暴露的公共方法
    returns: dict
     - html: 解析后的html
     - char_size： 解析后的html长度
     - token_size： 解析后的html token长度
    """
    if not html or not isinstance(html, str):
      return {"html": "", "char_size": 0, "token_size": 0}
    
    # 串行调用其他方法
    html = self._body(html)
    html = self._shake(html)
    html = self._minify(html)
    
    # 计算字符长度
    char_size = len(html)
    
    # 计算token数量
    token_size = self._count_tokens(html)
    
    return {
      "html": html,
      "char_size": char_size,
      "token_size": token_size
    }
  
  def _count_tokens(self, text: str) -> int:
    """
    计算文本的token数量
    使用tiktoken库进行计算
    """
    try:
      # 使用cl100k_base编码（GPT-4、GPT-3.5-Turbo等使用的编码）
      encoding = tiktoken.get_encoding("cl100k_base")
      tokens = encoding.encode(text)
      return len(tokens)
    except Exception as e:
      # 如果出现异常，返回字符长度作为备选
      return len(text)
  
  def _body(self,html:str)->str:
    """
    [Protected] 提取html的body内容
    - 移除所有head元素
    - 移除指定的不需要的标签：style、script、iframe、frame、canvas、svg
    - 移除所有注释
    """
    if not html or not isinstance(html, str):
      return ""
      
    # 解析HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # 提取body内容，如果没有body则使用整个文档
    body = soup.body
    if body:
      soup = BeautifulSoup(str(body), 'html.parser')
    
    # 定义需要移除的标签列表，方便统一管理和修改
    tags_to_remove = ['style', 'script', 'iframe', 'frame', 'canvas', 'svg', 'footer', 'aside']
    
    # 统一移除所有指定的标签
    for tag_name in tags_to_remove:
      for tag in soup(tag_name):
        tag.decompose()
    
    # 移除所有注释
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
      comment.extract()
    
    # 空白字符的处理将在_minify方法中进行
    return str(soup)
    
  def _shake(self,html:str)->str:
    """
    [Protected] 移除非必要属性，减少总字符数量
    - 移除所有标签内的非必要属性，例如 style class id 等
    - 保留某些必须的属性，例如 href src alt 等
    - 移除样式类标签 strong、b、i，但保留标签内的文本内容
    """
    if not html or not isinstance(html, str):
      return ""
      
    # 定义要保留的属性
    keep_attributes = {'href', 'src', 'alt', 'title'}
    
    # 解析HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # 移除样式类标签 strong、b、i，但保留标签内的文本内容
    style_tags = ['strong', 'b', 'i']
    for tag_name in style_tags:
      for tag in soup.find_all(tag_name):
        tag.unwrap()  # 移除标签但保留内容
    
    # 遍历所有标签
    for tag in soup.find_all(True):
      # 创建一个新的字典，只保留必要的属性
      new_attrs = {}
      for attr, value in tag.attrs.items():
        if attr.lower() in keep_attributes:
          new_attrs[attr] = value
      
      # 替换属性
      tag.attrs = new_attrs
    
    # 返回清理后的HTML
    return str(soup)
    
  def _minify(self, html: str) -> str:
    """
    [Protected] 最小化HTML内容
    - 移除所有不必要的空白
    - 移除所有注释
    - 压缩标签间的空白
    """
    if not html or not isinstance(html, str):
      return ""
    
    # 移除注释
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    # 压缩空白字符
    html = re.sub(r'\s+', ' ', html)
    # 移除标签间的空白
    html = re.sub(r'>\s+<', '><', html)
    # 移除首尾空白
    html = html.strip()
    
    return html