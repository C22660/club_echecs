from .controllers import home



def main():
    app = home.ApplicationController()
    app.start()




if __name__ == '__main__':
    main()