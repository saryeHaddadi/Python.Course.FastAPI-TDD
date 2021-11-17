import uvicorn
from web.Configuration import Configuration
from web.ApplicationBuilder import ApplicationBuilder



def main():
    uvicorn.run('main:build_app', factory=True, host='127.0.0.1', port=8000, reload=True)

def build_app(configuration: Configuration = Configuration()):
    return ApplicationBuilder(configuration).build()

if __name__ == '__main__':
    main()




