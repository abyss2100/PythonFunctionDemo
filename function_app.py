import logging
import azure.functions as func
from main import run_main

app = func.FunctionApp()

@app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def AzureFuncDemo(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')
    run_main()
    logging.info('Python timer trigger function executed.')