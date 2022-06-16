
from dis import dis
from msilib.schema import LockPermissions


hr_1=60
day_1=hr_1 * 24 
week_1=day_1 * 7
week_7=week_1 * 7
print(week_7)

print(2* 1 *10*-2)
print(299792458 * 1 * 10 **-9)
print(299792458 *100 *1/1000000000)
#the distance that light travels in my processor cycle given that it has  a clock speed of 2.5GHZ   
Speed_of_light=299792458
Clock_speed=2500000000
distance= Speed_of_light/Clock_speed
print(distance * 100 ,"cm")



a='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos 
sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
recusandae alias error harum maxime adipisci amet laborum. Perspiciatis 
minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit 
quibusdam sed amet tempora. Sit laborum ab, eius fugit doloribus tenetur 
fugiat, temporibus enim commodi iusto libero magni deleniti quod quam 
consequuntur! Commodi minima excepturi repudiandae velit hic maxime
doloremque. Quaerat provident commodi consectetur veniam similique ad 
earum omnis ipsum saepe, voluptas, hic voluptates pariatur est explicabo 
fugiat, dolorum eligendi quam cupiditate excepturi mollitia maiores labore 
suscipit quas? Nulla, placeat. Voluptatem quaerat non architecto ab laudantium
modi minima sunt esse temporibus sint culpa, recusandae aliquam numquam 
totam ratione voluptas quod exercitationem fuga. Possimus quis earum veniam 
quasi aliquam eligendi, placeat qui corporis!'''
print(a[-1:])
print(a[:3] +a[3:])
print(a[:])

print(a.find("Lorem"),type(a))