import datetime
from typing import List
import numpy as np
import streamlit as st

from viz import image_show, daily_scatter, weekday_bar
from os import listdir
from os.path import isfile, join
import random
import time


def write():

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            # When Random Love Hits

            ### It hits hard
            ### So Reality would look like a order Chaos 
            .
            ### It breaks rules
            ### So an Ostriche can become a Flamingo 🦩

            """
        )

    with col2:
        mypath = "/home/ai2/antonio/Chat/pics"
        onlyfiles = [
            mypath + "/" + f for f in listdir(mypath) if isfile(join(mypath, f))
        ]
        random_path = random.choice(onlyfiles)
        image = image_show(random_path)
        st.plotly_chart(image, theme="streamlit", use_container_width=True)


#     if st.checkbox("Want more Info about the models? Check me!"):
#         st.markdown(
#             """
#             ### Arabic Propaganda Detection
#             TODO

#             ### Arabic Subjectivity Detection
#             TODO

#             ### Arabic Stance Detection
#             """
#         )
#     # put checkboxes for each model
#     st.sidebar.header("Select the models you want to use")
#     subjectivity = st.sidebar.checkbox("Subjectivity Detection", value=True)
#     propaganda = st.sidebar.checkbox("Propaganda Detection", value=True)
#     stance = st.sidebar.checkbox("Stance Detection", value=True)

#     st.sidebar.header("Other options")
#     detailed_results = st.sidebar.checkbox("Show detailed results", value=False)

#     st.sidebar.header("Feedback Guidelines for Propaganda and Subjectivity 👇")
#     st.sidebar.markdown(
#         """
#         #### What kind of language is the speaker using?
#         TODO

#         """
#     )

#     if subjectivity or propaganda or stance:
#         if "input_text" not in st.session_state:
#             st.session_state.input_text = ""

#         input_text = st.text_area(
#             "Enter text to Article you want to test on",
#             "بُدئ العمل بالبرنامج قبل 3 سنوات، وتطوّر لاحقاً ليشمل إنشاء مواقع إلكترونية لتلقّي لقاحات كورونا وطلب أذونات للتنقل خلال فترة الحجر المنزلي، ثم إنشاء منصة impact التي سجّل المواطنون عبرها طلبات للحصول على البطاقة التمويلية وبرنامج شبكة الأمان الاجتماعي. لكن، لأسباب غير واضحة، وقّع رئيس التفتيش والسفير البريطاني في لبنان إيان كولارد مذكّرة التفاهم في أيلول 2021، أي بعد مرور نحو عام ونصف عام على بدء العمل بها. هذه العلاقة الملتبسة بين عطية والسفارة البريطانية دفعت رئاسة الحكومة، أخيراً، إلى تحويل الملف الى ديوان المحاسبة والنيابة العامة التمييزية، تضمّن طلب الإضاءة على عدة نقاط لناحية «كشف داتا اللبنانيين أمام جهات غير رسمية والتلاعب والمُحاباة في اختيار المستفيدين من برنامج شبكة الأمان الاجتماعي وعدم الاستجابة لطلب الأجهزة الأمنية بالاطّلاع على منصة impact التي لا تسمح سوى لموظفي الشركة البريطانية بالوصول إلى قاعدة البيانات الخاصة بالمنصة». المذكّرة التي وقّعها عطية وكولارد، ولم تُعرض على أي جهة رسمية، نصّت على تخصيص السفارة 2.5 مليون جنيه إسترليني (نحو ثلاثة ملايين دولار) مقابل التزام التفتيش بالعمل مع السفارة والشركة المكلّفة من قبلها («سايرن») بشفافية و«الاستجابة لطلباتهما بمرونة وفعالية وضمن مهل زمنية محددة». علماً أن هذه «المعاهدة» بين مؤسسة لبنانية وسفارة أجنبية لم يكلف رئيس التفتيش نفسه عناء عرضها على وزارتي الخارجية والعدل أو الأمانة العامة لمجلس الوزراء لتحيلها إلى الحكومة وإصدار قرار بالموافقة عليها. بدلاً من ذلك، ارتأى عطية صرف أموال ما سماها «هبة بريطانية» من تلقاء نفسه، ومن دون تطبيق المسار القانوني الذي يفرضه الدستور في حالات مماثلة، ومن دون التصريح عن طرق صرفها. كما فتح أبواب إدارته أمام مهندسي الشركة البريطانية للتحكم بكل مفاصل المنصة، وما يعني ذلك «تعرية» الأسر اللبنانية تماماً عبر الاطّلاع على أرقام الحسابات المصرفية لأفرادها ورواتبهم ومساحات منازلهم وأرقام سياراتهم وما إذا كانوا يملكون براداً أو غسالة وصولاً إلى عدد سفراتهم ووجهاتهم وأدقّ التفاصيل المتعلقة بحياتهم اليومية. حصل ذلك كله على مدى 3 سنوات، وسط صمت مريب من الحكومة ومجلس النواب وكل المسؤولين، رغم مراسلات الأجهزة الأمنية. ولم يكن رئيس الحكومة ليتحرك لولا أن عطية، ولسبب غير واضح، قرّر في 5/4/2022، أي بعد 5 أيام على تاريخ انتهاء المذكّرة مع «سايرن»، إبلاغ رئاسة مجلس الوزراء بها عبر كتاب أرفق فيه نسخة عن المذكّرة طالباً «الاطّلاع وتقرير المناسب آملين الموافقة على قبول هذا الدعم التقني والفني المقدّم لرفع قدرات التفتيش المركزي لما فيه من خير على العمل الرقابي والإداري وخدمة الوطن والمواطن».",
#             height=250,
#         )
#         stance_claim = None
#     if stance:
#         if "stance_claim" not in st.session_state:
#             st.session_state.stance_claim = ""
#         stance_claim = st.text_area(
#             "Enter the text of the tested Claim",
#             "باع القاضي بيطار معلومات اللبنانيين إلى السفارة البريطانية",
#         )

#     predict_btn = st.button("Predict")

#     if "predict_btn_state" not in st.session_state:
#         st.session_state.predict_btn_state = False

#     if predict_btn or st.session_state.predict_btn_state:
#         st.session_state.predict_btn_state = True
#         predict_btn = False
#         if (
#             input_text != st.session_state.input_text
#             or stance_claim != st.session_state.stance_claim
#         ):
#             st.session_state.input_text = input_text
#             st.session_state.stance_claim = stance_claim
#             new_text = True
#             logger.info("New Input text detected")
#         else:
#             new_text = False
#             logger.info("No new Input text detected")

#         if "request_id" not in st.session_state or new_text:
#             st.session_state.request_id = "MDLDEMOFE_" + str(uuid.uuid4())

#         input_text_list = sent_tokenize(
#             input_text.replace("...", ".").replace("..", ".")
#         )

#         if not new_text and detailed_results:
#             detailed_score_dict = {}
#             for i, _ in enumerate(input_text_list):
#                 text = input_text_list[i]
#                 detailed_score_dict[text] = {}
#                 if subjectivity:
#                     detailed_score_dict[text]["subjectivity"] = {
#                         "label": st.session_state.subj_results[i][0].label,
#                         "score": st.session_state.subj_results[i][0].score,
#                     }
#                 if propaganda:
#                     detailed_score_dict[text]["propaganda"] = {
#                         "label": st.session_state.prop_results[i][0].label,
#                         "score": st.session_state.prop_results[i][0].score,
#                     }
#                 if stance:
#                     detailed_score_dict[text]["stance"] = {
#                         "label": st.session_state.stance_results[i][0].label,
#                         "score": st.session_state.stance_results[i][0].score,
#                     }

#             st.write(detailed_score_dict)

#         cols = st.columns(3)
#         with cols[0]:
#             if propaganda:
#                 selected_client = propaganda_client
#                 if new_text:
#                     prop_results: List[
#                         List[TextClassificationOutput]
#                     ] = selected_client.run_inference(
#                         input_text_list, request_id=st.session_state.request_id
#                     )
#                     st.session_state.prop_results = prop_results
#                 else:
#                     prop_results = st.session_state.prop_results

#                 results_string = "\n".join(str(x) for x in prop_results)
#                 logger.info(f"Propaganda Results: \n{str(results_string)}")

#                 average_pop_score = sum(
#                     [
#                         x[0].score if x[0].label == "PROPAGANDA" else x[1].score
#                         for x in prop_results
#                     ]
#                 ) / len(prop_results)

#                 logger.info(st.session_state.request_id)
#                 st.write(f"Average Propaganda Score: `{average_pop_score}`")

#                 propaganda_fig = gauge_meter(proba=average_pop_score, title="")
#                 st.plotly_chart(
#                     propaganda_fig, theme="streamlit", use_container_width=True
#                 )
#                 # # put feedback UI
#                 # with st.form("prop_feedback_form"):
#                 #     st.session_state.prop_feedback = st.radio(
#                 #         "What do you think the model's prediction should be?",
#                 #         (
#                 #             "Propaganda",
#                 #             "Not Propaganda",
#                 #             "Can't tell",
#                 #             "It's correct",
#                 #         ),
#                 #         index=3,
#                 #     )

#                 #     st.session_state.prop_submitted = st.form_submit_button(
#                 #         "Submit Feedback",
#                 #     )

#                 # if st.session_state.prop_submitted:
#                 #     logger.info(f"Prop Feedback: {st.session_state.prop_feedback}")
#                 #     prop_results_feedback = FeedbackDocument(
#                 #         uuid=st.session_state.request_id,
#                 #         model_name=selected_client.config.model_name,
#                 #         model_version=selected_client.config.model_version,
#                 #         model_input=input_text,
#                 #         date_created=datetime.datetime.now(),
#                 #         provided_label=st.session_state.prop_feedback,
#                 #     )
#                 #     # todo: update model output to support list of sentences
#                 #     prop_results_feedback.update_model_output(
#                 #         st.session_state.prop_results
#                 #     )
#                 #     prop_results_feedback.save()
#                 #     logger.info(f"Feedback saved: {prop_results_feedback}")
#                 # print(prop_results_feedback)

#             # else:
#             #     temp = st.session_state.pop("prop_results")

#         with cols[1]:
#             if subjectivity:
#                 selected_client = subjectivity_client
#                 if new_text:
#                     subj_results: List[
#                         List[TextClassificationOutput]
#                     ] = selected_client.run_inference(
#                         input_text_list, request_id=st.session_state.request_id
#                     )

#                     st.session_state.subj_results = subj_results
#                 else:
#                     subj_results = st.session_state.subj_results

#                 results_string = "\n".join(str(x) for x in subj_results)
#                 logger.info(f"Subjectivity Results: \n{results_string}")

#                 average_subj_score = sum(
#                     [
#                         x[0].score if x[0].label == "SUBJECTIVE" else x[1].score
#                         for x in subj_results
#                     ]
#                 ) / len(subj_results)

#                 logger.info(st.session_state.request_id)
#                 st.write(f"Average Subjective Score: `{average_subj_score}`")
#                 subj_fig = gauge_meter(proba=average_subj_score, title="")
#                 st.plotly_chart(subj_fig, theme="streamlit", use_container_width=True)

#                 # put feedback UI
#                 # with st.form("subj_feedback_form"):
#                 #     st.session_state.subj_feedback = st.radio(
#                 #         "What do you think the model's prediction should be?",
#                 #         (
#                 #             "Propaganda",
#                 #             "Not Propaganda",
#                 #             "Can't tell",
#                 #             "It's correct",
#                 #         ),
#                 #         index=3,
#                 #     )

#                 #     st.session_state.subj_submitted = st.form_submit_button(
#                 #         "Submit Feedback",
#                 #     )
#                 # if st.session_state.subj_submitted:
#                 #     logger.info(
#                 #         f"Subjectivity Feedback: {st.session_state.subj_feedback}"
#                 #     )
#                 #     subj_results_feedback = FeedbackDocument(
#                 #         uuid=st.session_state.request_id,
#                 #         model_name=selected_client.config.model_name,
#                 #         model_version=selected_client.config.model_version,
#                 #         model_input=input_text,
#                 #         date_created=datetime.datetime.now(),
#                 #         provided_label=st.session_state.subj_feedback,
#                 #     )
#                 #     # todo: update model output to support list of sentences
#                 #     subj_results_feedback.update_model_output(
#                 #         st.session_state.subj_results
#                 #     )
#                 #     subj_results_feedback.save()
#                 #     logger.info(f"Feedback saved: {subj_results_feedback}")
#                 # print(prop_results_feedback)
#             # else:
#             #     temp = st.session_state.pop("subj_results")

#         with cols[2]:
#             if stance:
#                 selected_client = stance_client
#                 if new_text:
#                     # stance_result: List[
#                     #     List[TextClassificationOutput]
#                     # ] = selected_client.run_inference(
#                     #     input_text, stance_claim, request_id=st.session_state.request_id
#                     # )

#                     # st.session_state.stance_result = stance_result
#                     agree = random.randint(7000, 10000)
#                     diagree = random.randint(500, 2000)
#                     related = random.randint(2000, 5000)
#                     unrelated = random.randint(100, 1000)
#                     summ = sum([agree, diagree, related, unrelated])
#                     agree /= summ
#                     diagree /= summ
#                     related /= summ
#                     unrelated /= summ
#                     stance_result = {
#                         "Agree": agree,
#                         "Disagree": diagree,
#                         "Discuss": related,
#                         "Unrelated": unrelated,
#                     }
#                     st.session_state.stance_result = stance_result
#                     logger.info("session_state.stance_result allocated")
#                 else:
#                     logger.info("stance_result allocated with session state")
#                     stance_result = st.session_state.stance_result

#                 results_string = "\n".join(
#                     f"{x}:{stance_result[x]}" for x in stance_result
#                 )
#                 logger.info(f"Stance Results: \n{results_string}")

#                 idx = np.argmax(list(stance_result.values()))
#                 label = list(stance_result.keys())[idx]
#                 proba = list(stance_result.values())[idx]

#                 logger.info(st.session_state.request_id)
#                 st.write(f"{label} Score: `{proba}`")
#                 stance_fig = heat_map(proba=stance_result, title="")
#                 st.plotly_chart(stance_fig, theme="streamlit", use_container_width=True)

#                 # put feedback UI
#                 # with st.form("subj_feedback_form"):
#                 #     st.session_state.subj_feedback = st.radio(
#                 #         "What do you think the model's prediction should be?",
#                 #         (
#                 #             "Propaganda",
#                 #             "Not Propaganda",
#                 #             "Can't tell",
#                 #             "It's correct",
#                 #         ),
#                 #         index=3,
#                 #     )

#                 #     st.session_state.subj_submitted = st.form_submit_button(
#                 #         "Submit Feedback",
#                 #     )
#                 # if st.session_state.subj_submitted:
#                 #     logger.info(
#                 #         f"Subjectivity Feedback: {st.session_state.subj_feedback}"
#                 #     )
#                 #     subj_results_feedback = FeedbackDocument(
#                 #         uuid=st.session_state.request_id,
#                 #         model_name=selected_client.config.model_name,
#                 #         model_version=selected_client.config.model_version,
#                 #         model_input=input_text,
#                 #         date_created=datetime.datetime.now(),
#                 #         provided_label=st.session_state.subj_feedback,
#                 #     )
#                 #     # todo: update model output to support list of sentences
#                 #     subj_results_feedback.update_model_output(
#                 #         st.session_state.subj_results
#                 #     )
#                 #     subj_results_feedback.save()
#                 #     logger.info(f"Feedback saved: {subj_results_feedback}")
#                 # print(prop_results_feedback)
#             # else:
#             #     temp = st.session_state.pop("subj_results")


# # %%impo
