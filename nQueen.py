from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel,  QMainWindow
import sys

#create a class for the main window
class MainWindow(QMainWindow):
    def __init__(self, n=None):
        super().__init__()

        #create 2D array to store the board with n number user input
        n = int(input("Enter the number of queens: "))
        print("The solution is: " + str(n))
        board = [[0 for x in range(n)] for y in range(n)]
        self.num = n
        # place n queens on the board using backtracking algorithm
        def nQueen(board, col):
            if col >= n:
                return True
            for i in range(n):
                if isSafe(board, i, col):
                    board[i][col] = 1
                    if nQueen(board, col + 1):
                        return True
                    board[i][col] = 0
            return False

        # check if the queen can be placed at the given row and column
        def isSafe(board, row, col):
            for i in range(col):
                if board[row][i] == 1:
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            return True

        self.board = board
        nQueen(self.board, 0)
        # print the board
        for i in range(n):
            for j in range(n):
                print(self.board[i][j], end=" ")
            print()

        #set the window properties
        self.setWindowTitle("N-Queens " + str(n) + "x" + str(n))
        self.setGeometry(100, 100, 300, 300)
        self.setStyleSheet("background-color: #f0f0f0")

        self.showboard()
    def get_value(self):
        return print(self.board)

    def showboard(self ):
        self.setBoard()
        self.resize(self.boardSize * self.num, self.boardSize * self.num)

    def setBoard(self):
        self.tileSize = 75
        self.boardSize =self.tileSize

        #replace the images to the board with the queens
        for i in range(self.num):
            for j in range(self.num):
                if self.board[i][j] == 1:
                    label = QLabel(self)
                    queen = QPixmap("./images/bq.png")
                    label.setPixmap(queen)
                    label.setGeometry(j * self.tileSize, i * self.tileSize, self.tileSize, self.tileSize)
                    label.setScaledContents(True)
                    label.move(j * self.tileSize, i * self.tileSize)
                    self.board[i][j] = label
                else:
                    label = QLabel(self)
                    br = QPixmap("./images/wt.png")
                    label.setPixmap(br)
                    label.setGeometry(j * self.tileSize, i * self.tileSize, self.tileSize, self.tileSize)
                    label.setScaledContents(True)
                    label.move(j * self.tileSize, i * self.tileSize)
                    self.board[i][j] = label



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

