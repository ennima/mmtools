seconds = 170.51199984550476
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print ("%d:%02d:%02d" % (h, m, s))