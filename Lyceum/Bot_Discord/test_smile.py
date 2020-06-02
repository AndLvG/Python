from emoji import emojize
from random import choice
import emoji

SMILE = ['grinning_face:', ':grinning_face_with_big_eyes:', ':grinning_face_with_smiling_eyes:',
         ':beaming_face_with_smiling_eyes:', ':grinning_squinting_face:', ':grinning_face_with_sweat:',
         ':rolling_on_the_floor_laughing:', ':face_with_tears_of_joy:', ':slightly_smiling_face:', ':upside-down_face:',
         ':winking_face:', ':smiling_face_with_smiling_eyes:', ':smiling_face_with_halo:',
         ':smiling_face_with_3_hearts:', ':smiling_face_with_heart-eyes:', ':star-struck:', ':face_blowing_a_kiss:',
         ':kissing_face:', ':smiling_face:', ':kissing_face_with_closed_eyes:', ':kissing_face_with_smiling_eyes:',
         ':face_savoring_food:', ':face_with_tongue:', ':winking_face_with_tongue:', ':zany_face:',
         ':squinting_face_with_tongue:', ':money-mouth_face:', ':hugging_face:', ':face_with_hand_over_mouth:',
         ':shushing_face:', ':thinking_face:', ':zipper-mouth_face:', ':face_with_raised_eyebrow:', ':neutral_face:',
         ':expressionless_face:', ':face_without_mouth:', ':smirking_face:', ':unamused_face:',
         ':face_with_rolling_eyes:', ':grimacing_face:', ':lying_face:', ':relieved_face:', ':pensive_face:',
         ':sleepy_face:', ':drooling_face:', ':sleeping_face:', ':face_with_medical_mask:', ':face_with_thermometer:',
         ':face_with_head-bandage:', ':nauseated_face:']


smile = emojize(choice(SMILE), use_aliases=True)
for s in SMILE:
    print(emojize(s, use_aliases=True))
print(emoji.UNICODE_EMOJI)

# pip install emoji
