# op_cart_test
一个用于练习的基于Selenium + Page Object Mode + pytest构建的关于OpenCart开源电商项目的测试框架

分层架构: 采用经典的 Page Object Model 设计模式，实现代码高可维护性和低耦合度

数据驱动: 通过 Excel 管理测试数据，实现测试用例与数据的分离

多浏览器支持: 内置 Chrome 和 Firefox 浏览器支持，轻松扩展其他浏览器

模块化设计: 将页面元素、操作和业务流程完全分离，便于团队协作

pytest 集成: 使用业界领先的 pytest 测试框架，支持参数化测试和丰富的插件生态

技术栈：
编程语言: Python 3.7+
测试框架: pytest
浏览器自动化: Selenium WebDriver
数据管理: pandas + openpyxl
元素定位: XPath, CSS Selector, ID, Name 等共8种全部定位策略
报告生成: Allure Report (可扩展)
