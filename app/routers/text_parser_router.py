from flask import request
from services.text_service import TextService

class TextRouter():
    """Class handling HTTP validations from request."""

    def __init__(self, text_service):
        self.text_service = text_service

    def words_count(self):
        body = request.json

        if "text" not in body:
            return "bad request", 400

        response = self.text_service.agg_words_count(
            body["text"],
        )

        fmt_response = {
            "aggregation": [
                {"word": word, "count": int(count)} for word, count in response
            ]
        }

        return fmt_response, 200

    def words_number(self):
        body = request.json

        if "text" not in body:
            return "bad request", 400

        response = self.text_service.agg_words_number(
            body["text"],
        )

        fmt_response = {
            "number_of_words": response
        }

        return fmt_response, 200

    def full_text_length(self):
        body = request.json

        if "text" not in body:
            return "bad request", 400

        length, no_spaces_length = self.text_service.text_length(
            body["text"],
        )

        fmt_response = {
            "text_length": {
                "with_spaces": length,
                "with_no_spaces": no_spaces_length,
            }
        }

        return fmt_response, 200


    def text_statistic(self):
        body = request.json

        if "text" not in body:
            return "bad request", 400

        words_count = self.text_service.agg_words_count(
            body["text"],
        )

        fmt_response = {
            "aggregation": [
                {"word": word, "count": int(count)} for word, count in words_count
            ]
        }

        fmt_response["number_of_words"] = self.text_service.agg_words_number(
            body["text"],
        )

        length, no_spaces_length = self.text_service.text_length(
            body["text"],
        )

        fmt_response["text_length"] = {
                "with_spaces": length,
                "with_no_spaces": no_spaces_length,
        }

        return fmt_response, 200
