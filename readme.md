

五岳科技网上阅卷简单的鼠标点击模拟键盘输入模拟自动评分

针对试卷批阅网站：https://www.wylkyj.com/yuejuan/#/projectList

ocr网站：https://web.baimiaoapp.com/

截屏工具：Snipaste

---

$ python -m venv env  **# Windows**

$ env\S**cripts**\activate  **# Windows**

pip install -r requirements.txt

---

评分规则自定义

keyword*count为关键字个数 char*count为字符总个数 书写逻辑，

1.如果关键字个数为0，看字数由0-10则 score =0，10-50则 score =1， 50-100则 score =2，100-250则 score =3，250以上score =4

2.如果关键字个数为1到2，看字数由0-100则 score =3，100-200则 score =4，200以上则 score =5，

3.如果关键字个数为3个，看字数由0-200则 score =4，200-250则 score =5，250以上则 score =6，

4.如果关键字个数为3个以上，看字数由0-200则 score =5，200-300则 score =6，300以上则 score =7，

---
