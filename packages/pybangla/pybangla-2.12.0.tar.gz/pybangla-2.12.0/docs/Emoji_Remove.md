# 4. Emoji Removal
Now our normalizer can be used for removing emojis.

```py
text = 'দয়া করে পবিত্র কুরআনুল কারিম বলেন,,,,পবিত্র কথাটা অবশ্যই বলবেন,,, প্লিজ 😢😥🙏🙏🙏'
text = nrml.remove_emoji(text)
print(f"{text}")

#output:
দয়া করে পবিত্র কুরআনুল কারিম বলেন,,,,পবিত্র কথাটা অবশ্যই বলবেন,,, প্লিজ
```


```py
text = "😬😬 আর বিভিন্ন চ্যানেল সম্পর্কে কি বলব"
text = nrml.remove_emoji(text)
print(f"{text}")

#output:
 আর বিভিন্ন চ্যানেল সম্পর্কে কি বলব
```