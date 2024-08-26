from __future__ import annotations

import pendulum
from airflow.decorators import task
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor 
import tsslogging
import os
from datetime import datetime, timedelta
import importlib  
from airflow.operators.python import (
    ExternalPythonOperator,
    PythonOperator
)
step1 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step2 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step3 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step4 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step5 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step6 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step7 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step8 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step9 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")
step10 = importlib.import_module("tml-solutions.myawesometmlsolution.tml-system-step-1-getparams-dag-myawesometmlsolution")

# TML Solution template for processing
# Use this DAG to start processing data with:
# 1. visualization
# 2. containerization
# 3. documentationa


with DAG(
    dag_id="solution_preprocessing_dag_myawesometmlsolution",
    start_date = pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=None,
    schedule_interval="@once"
) as dag:
  start_task = BashOperator(
    task_id="start_tasks_tml_preprocessing",
    bash_command="echo 'Start task'",
  )
# STEP 1: Get the Parameters
  sensor_A = PythonOperator(
            task_id="solution_task_getparams",
            python_callable=step1.getparams,
            provide_context=True,
            #python=PATH_TO_PYTHON_BINARY,
  )

# STEP 2: Create the Kafka topics
  sensor_B = ExternalTaskSensor(
      task_id="solution_task_createtopic",
      external_dag_id="tml_system_step_2_kafka_createtopic_dag_myawesometmlsolution",
      external_task_id="setupkafkatopics",
  )
# STEP 3: Produce data to topic        
  sensor_C = ExternalTaskSensor(
      task_id="solution_task_producetotopic",
      external_dag_id="tml_localfile_step_3_kafka_producetotopic_dag_myawesometmlsolution",
      external_task_id="readdata",
  )
# STEP 4: Preprocess the data        
  sensor_D = ExternalTaskSensor(
      task_id="solution_task_preprocess",
      external_dag_id="tml_system_step_4_kafka_preprocess_dag_myawesometmlsolution",
      external_task_id="processtransactiondata",
  )
  sensor_E = ExternalTaskSensor(
      task_id="solution_task_visualization",
      external_dag_id="tml_system_step_7_kafka_visualization_dag_myawesometmlsolution",
      external_task_id="startstreamingengine",
  )
# STEP 8: Containerize the solution        
  sensor_F = ExternalTaskSensor(
      task_id="solution_task_containerize",
      external_dag_id="tml_system_step_8_deploy_solution_to_docker_dag_myawesometmlsolution",
      external_task_id="dockerit",
  )
  start_task2 = BashOperator(
    task_id="Starting_Docker",
    bash_command="echo 'Start task Completed'",
  )    
  start_task3 = BashOperator(
    task_id="Starting_Documentation",
    bash_command="echo 'Start task Completed'",
  )
  start_task4 = BashOperator(
    task_id="Completed_TML_Setup_Now_Spawn_Main_Processes",
    bash_command="echo 'Start task Completed'",
  )
# STEP 10: Document the solution
  sensor_G = ExternalTaskSensor(
      task_id="solution_task_document",
      external_dag_id="tml_system_step_10_documentation_dag_myawesometmlsolution",
      external_task_id="generatedoc",
  )

  start_task >> sensor_A >> sensor_B >> start_task2 >> sensor_F >> start_task3 >> sensor_G >> start_task4 >> [sensor_C, sensor_D, sensor_E]
