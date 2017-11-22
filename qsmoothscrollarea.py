from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,time,math

class QSmoothScrollArea(QtGui.QScrollArea):
    """docstring for QSmoothScrollArea"""
    def __init__(self, parent):
        super(QSmoothScrollArea, self).__init__(parent)
        self.lastWheelEvent = 0
        self.smoothMoveTimer = QTimer(self)
        self.smoothMoveTimer.timeout.connect(self.slotSmoothMove)

        self.m_fps = 200
        # self.m_fps = 90
        # self.m_duration = 200.0
        self.m_duration = 300.0
        self.m_smoothMode = "NO_SMOOTH"
        self.m_smoothMode = "LINEAR"
        self.m_smoothMode = "COSINE"
        self.m_smoothMode = "QUADRATIC"
        self.m_smoothMode = "CONSTANT"
        self.m_smoothMode = "EXP"
        self.m_acceleration = 2.5

        self.m_smallStepModifier = QtCore.Qt.SHIFT
        self.m_smallStepRatio = 1.0 / 5.0
        self.m_bigStepModifier = QtCore.Qt.ALT
        self.m_bigStepRatio = 5.0

        self.scrollStamps = []
        self.stepsLeftQueue = []

    def fps(self):
        return self.m_fps

    def setFps(self,fps):
        self.m_fps = fps

    def duration(self):
        return self.m_duration

    def setDuration(self,mesc):
        self.m_duration = mesc

    def smoothMode(self):
        return self.m_smoothMode

    def acceration(self):
        return self.m_acceleration

    def setAcceration(self,acceration):
        self.m_acceleration = acceration

    def smallStepRatio(self):
        return self.m_smallStepRatio

    def setSmallStepRatio(self,smallStepRatio):
        self.m_smallStepRatio = smallStepRatio

    def bigStepRatio(self):
        return self.m_bigStepRatio

    def setBigStepRatio(self,bigStepRatio):
        self.m_bigStepRatio = bigStepRatio

    def smallStepModifier(self):
        return self.m_smallStepModifier

    def setSmallStepModifier(self,smallStepModifier):
        self.m_smallStepModifier = smallStepModifier

    def bigStepModifier(self):
        return self.m_bigStepModifier

    def setBigStepModifier(self,bigStepModifier):
        self.m_bigStepModifier = bigStepModifier

    def wheelEvent(self,e):
        if(self.m_smoothMode == "NO_SMOOTH"):
            QtGui.QScrollArea.wheelEvent(e)
            return

        now = QtCore.QDateTime.currentDateTime().toMSecsSinceEpoch()
        self.scrollStamps.append(now)
        while True:
            if len(self.scrollStamps) and (now - self.scrollStamps[0])>500:
                del self.scrollStamps[0]
            else:
                break
        self.accerationRatio = min(len(self.scrollStamps)/15.0,1.0)

        if not self.lastWheelEvent:
            self.lastWheelEvent = QtGui.QWheelEvent(e)
        else:
            self.lastWheelEvent = e

        self.stepsTotal = self.m_fps * self.m_duration / 1000.0
        # print self.stepsTotal
        multiplier = 1.0
        if (QtGui.QApplication.keyboardModifiers() and self.smallStepModifier()):
            multiplier *= self.smallStepRatio()
        if (QtGui.QApplication.keyboardModifiers() and self.bigStepModifier()):
            multiplier *= self.bigStepRatio()
        delta = e.delta() * multiplier
        if (self.acceration() > 0):
            delta += delta * self.acceration() * self.accerationRatio

        if len(self.stepsLeftQueue):
            self.stepsLeftQueue = []

        self.stepsLeftQueue.append([delta, self.stepsTotal])
        self.smoothMoveTimer.start(1000.0 / self.m_fps)

    def slotSmoothMove(self):
        totalDelta = 0

        for it in self.stepsLeftQueue:
            totalDelta += self.subDelta(it[0], it[1])
            it[1] -= 1

        while (len(self.stepsLeftQueue) and self.stepsLeftQueue[0][1] == 0):
            del self.stepsLeftQueue[0]

        orientation = QtCore.Qt.Orientation(self.lastWheelEvent.orientation())
        if ((self.bigStepModifier() and QtCore.Qt.ALT) or 
            (self.smallStepModifier() and QtCore.Qt.ALT)):
            orientation = QtCore.Qt.Vertical

        # print len(self.stepsLeftQueue),round(totalDelta)
        e = QWheelEvent(
                    self.lastWheelEvent.pos(),
                    self.lastWheelEvent.globalPos(),
                    round(totalDelta),
                    self.lastWheelEvent.buttons(),
                    Qt.NoModifier,
                    orientation
        )
        if (e.orientation() == QtCore.Qt.Horizontal):
            QtGui.QApplication.sendEvent(self.horizontalScrollBar(), e)
        else:
            QtGui.QApplication.sendEvent(self.verticalScrollBar(), e)

        if not len(self.stepsLeftQueue):
            self.smoothMoveTimer.stop()

    def subDelta(self, delta, stepsLeft):
        # Q_ASSERT(m_smoothMode != NO_SMOOTH)

        m = self.stepsTotal / 2.0
        x = abs(self.stepsTotal - stepsLeft - m)

        if self.m_smoothMode == "NO_SMOOTH":
            return 0
            
        if self.m_smoothMode == "CONSTANT":
            return float(delta) / self.stepsTotal
            
        if self.m_smoothMode == "LINEAR":
            return 2.0*delta/self.stepsTotal * (m - x) / m
            
        if self.m_smoothMode == "QUADRATIC":
            return 3.0/4.0/m * (1.0 - x*x/m/m) * delta

        if self.m_smoothMode == "COSINE":
            return (math.cos(x * math.pi / m) + 1.0) / (2.0*m) * delta

        if self.m_smoothMode == "EXP":
            value = (math.cos(x * math.pi / m) + 1.0) / (2.0*m) * delta
            current_time = ((self.stepsTotal-stepsLeft)/self.stepsTotal * self.m_duration / 1000.0)
            
            def microsoft_pow_function(x):
                # return 0.06909 * pow(x, -2.018) / 4 / 140 * delta
                # return 0.04 * pow(x, -2.018) / 4 / 140 * delta # 90 fps
                return 0.05 * pow(x, -2.018) / 5 / 140 * delta # 200 fps

            value = microsoft_pow_function(current_time + 0.016667)
            return value
            
        return 0

class Windows(QtGui.QWidget):
    def __init__(self):
        super(Windows, self).__init__()
        self.setWindowTitle("QSmoothScrollArea Test Windows")
        self.scrollArea = QSmoothScrollArea(self)
        self.scrollArea2 = QScrollArea(self)
        
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.scrollArea,0,1)
        self.layout.addWidget(self.scrollArea2,0,0)
        self.layout.setContentsMargins(1,1,1,1)
        self.setLayout(self.layout)
     
        imageLabel = QLabel(self)
        imageLabel.setPixmap(QPixmap.fromImage(QImage("test.png")))
        self.scrollArea.setWidget(imageLabel)

        imageLabel2 = QLabel(self)
        imageLabel2.setPixmap(QPixmap.fromImage(QImage("test.png")))
        self.scrollArea2.setWidget(imageLabel2)

        # self.resize(1000,500)
        self.resize(248 * 2,480)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    w = Windows()
    w.show()
    sys.exit(app.exec_())
