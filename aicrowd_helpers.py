#!/usr/bin/env python
import aicrowd_api
import os

########################################################################
# Instatiate Event Notifier
########################################################################
aicrowd_events = aicrowd_api.events.AIcrowdEvents()


def execution_start():
    ########################################################################
    # Register Evaluation Start event
    ########################################################################
    aicrowd_events.register_event(
                event_type=aicrowd_events.AICROWD_EVENT_INFO,
                message="execution_started",
                payload={ #Arbitrary Payload
                    "event_type": "food_recognition_challenge:execution_started"
                    }
                )


def execution_progress(progress_payload):
    image_ids = progress_payload["image_ids"]
    ########################################################################
    # Register Evaluation Progress event
    ########################################################################
    aicrowd_events.register_event(
                event_type=aicrowd_events.AICROWD_EVENT_INFO,
                message="execution_progress",
                payload={ #Arbitrary Payload
                    "event_type": "food_recognition_challenge:execution_progress",
                    "image_ids" : image_ids
                    }
                )

def execution_success(payload):
    predictions_output_path = payload["predictions_output_path"]
    ########################################################################
    # Register Evaluation Complete event
    ########################################################################
    expected_output_path = os.getenv("AICROWD_PREDICTIONS_OUTPUT_PATH", False)
    if expected_output_path != predictions_output_path:
        raise Exception("Please write the output to the path specified in the environment variable : AICROWD_PREDICTIONS_OUTPUT_PATH instead of {}".format(predictions_output_path))

    aicrowd_events.register_event(
                event_type=aicrowd_events.AICROWD_EVENT_SUCCESS,
                message="execution_success",
                payload={ #Arbitrary Payload
                    "event_type": "food_recognition_challenge:execution_success",
                    "predictions_output_path" : predictions_output_path
                    },
                blocking=True
                )

def execution_error(error):
    ########################################################################
    # Register Evaluation Complete event
    ########################################################################
    aicrowd_events.register_event(
                event_type=aicrowd_events.AICROWD_EVENT_ERROR,
                message="execution_error",
                payload={ #Arbitrary Payload
                    "event_type": "food_recognition_challenge:execution_error",
                    "error" : error
                    },
                blocking=True
                )
