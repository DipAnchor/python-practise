# coding:utf8
my_name="Zed A. Shaw"
my_age= 35 # not a lie
my_height=float(74*2.54) #centimetre
my_weight=float(180*0.4535924) #kilo
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

print "Let's talk about %s." %my_name
print "He's %d centimetre tall." %my_height
print "He's %d kilos heavy." %my_weight

print "Actually that's not too heaby."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky ,try to get it exactly right
print "If I add %d,%d,and %d I get %d" %(my_age,my_height,my_weight,my_age+my_height+my_weight)