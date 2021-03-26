import zeep
from zeep import exceptions
import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow


class convert(QtWidgets.QMainWindow):
    def __init__(self):
        super(convert, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.convert.clicked.connect(self.convert)

    def convert(self):
        wsdl = 'http://nbg.gov.ge/currency.wsdl'
        client = zeep.Client(wsdl=wsdl)
        currency_in = self.ui.currency.currentText()
        amount_in = self.ui.amount.text()
        currency = client.service.GetCurrency(currency_in)
        result = float(currency) * float(amount_in)
        self.ui.result.setText(str(result))


app = QtWidgets.QApplication([])
application = convert()
application.show()

sys.exit(app.exec_())
