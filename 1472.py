class BrowserNode:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = BrowserNode(url = homepage)
        self.tail = self.head
        self.currentPage = self.head

    def visit(self, url: str) -> None:
        newPage = BrowserNode(url = url, prev = self.currentPage)
        self.currentPage.next = newPage
        self.currentPage = newPage
        self.tail = self.currentPage
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.currentPage.prev is not None:
                self.currentPage = self.currentPage.prev
        return self.currentPage.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.currentPage.next is not None:
                self.currentPage = self.currentPage.next
        return self.currentPage.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
