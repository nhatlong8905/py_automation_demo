import schedule
import subprocess

def job(): 
    subprocess.Popen(["pytest", "tests/report_temperature_test.py"])
schedule.every().day.hour.do(job).run()