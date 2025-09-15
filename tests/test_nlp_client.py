from src.nlp_client import query_openai
import json

transcript = """
CALLER: Hi, I’m calling about the property on Oak Street. I saw it online and wanted more details.

AI: Sure, I can help. What specifically would you like to know?

CALLER: First, what’s the square footage and how many bedrooms does it have?

AI: It’s 1,850 square feet with three bedrooms and two bathrooms.

CALLER: Okay, that sounds good. Is it still available?

AI: Yes, it’s currently on the market.

CALLER: Great. I’m also curious about the neighborhood — is it close to schools and grocery stores?

AI: Yes, it’s in a residential area about five minutes from the middle school and a large supermarket.

CALLER: That’s perfect. I’d like to set up a showing. Do you have any times this weekend?

AI: Saturday afternoon is open — would 2 PM work?

CALLER: Yes, that’s fine. Can you also send me information on any other homes in the $300k to $400k range nearby?

AI: Absolutely. I’ll email you three listings that match your budget and are within the same neighborhood.

CALLER: Thank you. What about the condition of the Oak Street house? Has it been renovated recently?

AI: Yes, the kitchen was remodeled last year, and the roof is brand new.

CALLER: Excellent. That makes it even more appealing.

AI: I’ll go ahead and confirm your Saturday showing and follow up with the additional listings.

CALLER: Will I get a reminder?

AI: Yes, I’ll send a text confirmation today and a reminder the day before your appointment.

CALLER: Perfect. That’s all I needed for now.

AI: Great. I’ll send the details shortly, and I’ll see you at the showing.

CALLER: Thanks so much.

AI: You’re welcome. Have a great day.

"""


rr_output = query_openai("reason_result", transcript)
rr_json = json.loads(rr_output)
reason = rr_json.get("reason")
result = rr_json.get("result")
summary = query_openai("summary", transcript)

print("Reason:", reason)
print("Result:", result)
print("SUMMARY:", summary)