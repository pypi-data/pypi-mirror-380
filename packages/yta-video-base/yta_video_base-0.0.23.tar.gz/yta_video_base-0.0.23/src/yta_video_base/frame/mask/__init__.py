"""
Extracted from official documentation:
- https://zulko.github.io/moviepy/getting_started/videoclips.html?highlight=mask#mask-clips

The fundamental difference between masks and standard clips is that standard clips output frames with 3 components (R-G-B) per pixel, comprised between 0 and 255, while a mask has just one composant per pixel, between 0 and 1 (1 indicating a fully visible pixel and 0 a transparent pixel). Seen otherwise, a mask is always in greyscale.
"""
from yta_video_base.video import Video
from yta_video_base.parser import VideoParser
from moviepy import CompositeVideoClip
from moviepy.Clip import Clip


# TODO: I think this will be deleted in the future,
# when refactored and when we confirm that here is
# another way of handling this
def apply_inverted_mask(
    video: Clip,
    mask_video: Clip
):
    """
    Applies the provided 'mask_video' with its mask inverted
    over the also provided 'video'. This is useful to make
    artistic effects. This methods applies the 
    'invert_video_mask' method to the provided 'mask_video'.
    """
    video = VideoParser.to_moviepy(video)
    # TODO: Do I need the mask? It is a mask clip not a clip
    # with a mask, so I think I don't...
    mask_video = VideoParser.to_moviepy(mask_video, do_include_mask = True)

    mask_video = Video(video = mask_video, is_mask = True).inverted
    # TODO: Handle durations
    final_clip = CompositeVideoClip([video, mask_video.with_subclip(0, video.duration)], use_bgclip = True)
    final_clip = final_clip.with_audio(video.audio)

    return final_clip