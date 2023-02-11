import datetime
import uuid
from typing import List

import awesome_streamlit as ast
import streamlit as st

def write():
    logger.info("Running Sentiment Topic")

    st.markdown(
        """
    # SIREN's Model Demo and Feedback Tool

    Enter the text you want to classify (in Arabic or English) and select the model you want to use (or all if you want).
    P.S. English is only supported for sentiment analysis.

    If you think the model is wrong, you can also provide feedback so we can improve it. Positive and negative feedback are both welcome.
    """
    )

    if st.checkbox("Want more Info about the models? Check me!"):
        st.markdown(
            """
            ### Arabic Sentiment Analysis
            This is a simple sentiment analysis app that uses the prediction kernel from Wissam's submission that won the [Arabic Senitment Analysis competition 2021 @ KAUST](https://www.kaggle.com/c/arabic-sentiment-analysis-2021-kaust)

            ### English Sentiment Analysis
            This model is based on BerTweet, a BERT-based model for sentiment analysis on Twitter. It was trained on the [TweetEval](https://github.com/cardiffnlp/tweeteval) dataset from 2020.

            ### Arabic Topic Classification
            This model is based on MarBERT (multi-dialectal Arabic BERT). It was trained on the [SANAD](https://www.sciencedirect.com/science/article/pii/S2352340919304305) a large dataset consisting of almost 200k new articles distributed into seven categories.

            """
        )

    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

    input_text = st.text_input("Enter text to classify", "ياي شو قوي هل موديل ")

    # put checkboxes for each model
    st.sidebar.header("Select the models you want to use")
    sentiment = st.sidebar.checkbox("Sentiment Analysis", value=True)
    topic = st.sidebar.checkbox("Topic Classification", value=True)
    st.sidebar.header("Other options")
    detailed_results = st.sidebar.checkbox("Show detailed results", value=False)

    st.sidebar.header("Feedback Guidelines for sentiment analysis 👇")
    st.sidebar.markdown(
        """
        #### What kind of language is the speaker using?

        1. the speaker is using positive language, for example, expressions of support, admiration, positive attitude, forgiveness, fostering, success, positive    emotional state

        2. the speaker is using negative language, for example, expressions of criticism, judgment, negative attitude, questioning validity/competence, failure, negative emotion

        3. the speaker is using expressions of sarcasm, ridicule, or mockery

        4. the speaker is using positive language in part and negative language in part

        5. the speaker is neither using positive language nor using negative language

        Notes:

        • A good response to this question is one that most people will agree with. For example, even if you think that sometimes the language can be considered negative, if you think most people will consider the language to be positive, then select the positive language option.

        • Agreeing or disagreeing with the speaker’s views should not have a bearing on your response. You are to assess the language being used (not the views). For example, given the tweet, ‘Evolution makes no sense’, the correct answer is ‘the speaker is using negative language’ since the speaker’s words are criticizing or judging negatively something (in this case the theory of evolution). Note that the answer is not contingent on whether you believe in evolution or not.
        """
    )
    predict_btn = st.button("Predict")

    if "predict_btn_state" not in st.session_state:
        st.session_state.predict_btn_state = False

    if predict_btn or st.session_state.predict_btn_state:
        st.session_state.predict_btn_state = True
        predict_btn = False
        if input_text != st.session_state.input_text:
            st.session_state.input_text = input_text
            new_text = True
            logger.info("New Input text detected")
        else:
            new_text = False
            logger.info("No new Input text detected")

        if "request_id" not in st.session_state or new_text:
            st.session_state.request_id = "MDLDEMOFE_" + str(uuid.uuid4())

        is_arabic = lang_id(input_text) == "ar"
        if is_arabic:
            st.write("Arabic Language detected")
        else:
            st.write("English Language detected")

        cols = st.columns(2)
        with cols[0]:
            if sentiment:
                selected_client = (
                    arabic_sentiment_client if is_arabic else english_sentiment_client
                )

                if new_text:

                    sa_results: List[
                        TextClassificationOutput
                    ] = selected_client.run_inference(
                        input_text, request_id=st.session_state.request_id
                    )
                    st.session_state.sa_results = sa_results

                else:
                    sa_results = st.session_state.sa_results

                logger.info(st.session_state.request_id)
                st.write(f"Sentiment: `{sa_results[0].label}`")
                if detailed_results:
                    detailed_sa_results = {x.label: x.score for x in sa_results}
                    st.write(detailed_sa_results)

                # put feedback UI
                with st.form("sa_feedback_form"):
                    st.session_state.sa_feedback = st.radio(
                        "What do you think the model's prediction should be?",
                        (
                            "Positive",
                            "Negative",
                            "Neutral",
                            "Mixed",
                            "Sarcasm",
                            "It's correct",
                        ),
                        index=3,
                    )

                    st.session_state.sa_submitted = st.form_submit_button(
                        "Submit Feedback"
                    )
                # if st.session_state.sa_submitted:
                #     logger.info(f"SA Feedback: {st.session_state.sa_feedback}")
                #     sa_results_feedback = FeedbackDocument(
                #         uuid=st.session_state.request_id,
                #         model_name=selected_client.config.model_name,
                #         model_version=selected_client.config.model_version,
                #         model_input=input_text,
                #         date_created=datetime.datetime.now(),
                #         provided_label=st.session_state.sa_feedback,
                #     )
                #     sa_results_feedback.update_model_output(st.session_state.sa_results)
                #     sa_results_feedback.save()
                #     logger.info(f"Feedback saved: {sa_results_feedback}")
                # # print(sa_results_feedback)

            else:
                temp = st.session_state.pop("sa_results")

        with cols[1]:
            if topic:
                if not is_arabic:
                    st.write(
                        "Since only Arabic is supported, we will pass your input through an Arabic model"
                    )

                selected_client = arabic_topic_client

                if new_text:
                    topic_results: List[
                        TextClassificationOutput
                    ] = selected_client.run_inference(
                        input_text, request_id=st.session_state.request_id
                    )
                    st.session_state.topic_results = topic_results
                else:
                    topic_results = st.session_state.topic_results

                logger.info(st.session_state.request_id)
                st.write(f"Topic: `{topic_results[0].label}`")
                if detailed_results:
                    detailed_topic_results = {x.label: x.score for x in topic_results}
                    st.write(detailed_topic_results)

                # put feedback UI
                with st.form("topic_feedback_form"):
                    st.write(
                        "What do you think the model's prediction should be? (Select all that apply)"
                    )
                    possible_topic_labels = [
                        "It's correct",
                        "Science & Technology",
                        "Business & Finance",
                        "Culture",
                        "Politics & News",
                        "Sports",
                        "Religion",
                        "Health",
                    ]

                    topic_label_ckboxes = []
                    for label in possible_topic_labels:
                        topic_label_ckboxes.append(st.checkbox(label))

                    st.session_state.topic_feedback = [
                        label
                        for label, checked in zip(
                            possible_topic_labels, topic_label_ckboxes
                        )
                        if checked
                    ]

                    st.session_state.topic_submitted = st.form_submit_button(
                        "Submit Feedback"
                    )
                # if st.session_state.topic_submitted:
                #     logger.info(f"Topic Feedback: {st.session_state.topic_feedback}")
                #     topic_results_feedback = FeedbackDocument(
                #         uuid=st.session_state.request_id,
                #         model_name=selected_client.config.model_name,
                #         model_version=selected_client.config.model_version,
                #         model_input=input_text,
                #         date_created=datetime.datetime.now(),
                #         provided_label=st.session_state.topic_feedback,
                #     )
                #     topic_results_feedback.update_model_output(
                #         st.session_state.topic_results
                #     )
                #     topic_results_feedback.save()
                #     logger.info(f"Feedback saved: {topic_results_feedback}")
                # # print(sa_results_feedback)
            else:
                temp = st.session_state.pop("topic_results")
