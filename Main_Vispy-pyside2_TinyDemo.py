from Ui_test_vispy import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import vispy.scene
from vispy.scene import visuals
import numpy as np

class IndexController(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # vispy.scene
        self.canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
        self.view = self.canvas.central_widget.add_view()
        #　addWidget
        self.verticalLayout_2.addWidget(self.canvas.native)
        self.pushButton.clicked.connect(self.showVispy)

    def showVispy(self):
        # generate data
        pos = np.random.normal(size=(100000, 3), scale=0.2)
        # one could stop here for the data generation, the rest is just to make the
        # data look more interesting. Copied over from magnify.py
        centers = np.random.normal(size=(50, 3))
        indexes = np.random.normal(size=100000, loc=centers.shape[0] / 2.,
                                   scale=centers.shape[0] / 3.)
        indexes = np.clip(indexes, 0, centers.shape[0] - 1).astype(int)
        scales = 10 ** (np.linspace(-2, 0.5, centers.shape[0]))[indexes][:, np.newaxis]
        pos *= scales
        pos += centers[indexes]

        # create scatter object and fill in the data
        scatter = visuals.Markers()
        scatter.set_data(pos, edge_color=None, face_color=(1, 1, 1, .5), size=5)

        self.view.add(scatter)

        self.view.camera = 'turntable'  # or try 'arcball'

        # add a colored 3D axis for orientation
        axis = visuals.XYZAxis(parent=self.view.scene)

if __name__ == '__main__':
    app = QApplication([])
    main = IndexController()
    main.show()
    # vispy.app.run()
    sys.exit(app.exec_())