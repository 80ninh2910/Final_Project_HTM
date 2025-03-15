from librarys.JSON_File_Factory import JsonFileFactory
from models.BOX.Movie import Movie
#NHÀ GIA TIÊN
movie=[]
name1="NHÀ GIA TIÊN"
type1="Comedy, Family T18"
dur1="117'"
des1="""
Manager: Huỳnh Lập
Performers: Huỳnh Lập, Phương Mỹ Chi, NSƯT Hạnh Thuý, NSƯT Huỳnh Đông, Puka, Đào Anh Tuấn, Trung Dân, Kiều Linh, Lê Nam, Chí Tâm, Thanh Thức, Trác Thuý Miêu, Mai Thế Hiệp, NS Mạnh Dung, NSƯT Thanh Dậu, NS Thanh Hiền, Nguyễn Anh Tú,…
Premiere: Friday, 21/02/2025

Tại sao chúng ta phải cùng nhau gìn giữ căn Nhà Gia Tiên? Vì sao những thế hệ con cháu luôn mất kết nối với ông bà của mình? Con người khi chết sẽ đi về đâu? Tại sao mỗi năm chúng ta phải làm đám giỗ cho người đã khuất?"""
ngt=Movie(name1,type1,dur1,des1)
movie.append(ngt)
#QUỶ NHẬP TRÀNG
name2="QUỶ NHẬP TRÀNG"
type2="HORROR T18"
dur2="122''"
des2="""
Manager: Pom Nguyễn
Performers: Khả Như, Quang Tuấn, Vân Dung, Trung Ruồi, Tân Trề, Phú Đôn, …
Premiere: Wednesday, 26/02/2025
MOVIE CONTENT:
The film is inspired by a true story and "the most horrifying legend about the dead coming back to life" - In a highland village, a couple Quang and Nhu make a living by burial. Their peaceful life is disturbed when they discover an ownerless coffin on their land. From here, strange phenomena begin to occur and haunt the whole village."""
qnt=Movie(name2,type2,dur2,des2)
movie.append(qnt)

#LITTLE EMMA
name3="LITTLE EMMA"
type3="COMEDY ,ADVENTURE P"
dur3="80''"
des3="""
Manager: Leo Lewis Liao
Performers: Travis Cloer, Niko Gerentes, Natalie Grace, ...
Premiere: Friday, 07/03/2025
MOVIE CONTENT:
A miniature girl raised by animal parents journeys to an island of tiny humans, uncovering unsettling revelations about her origins."""
emma=Movie(name3,type3,dur3,des3)
movie.append(emma)

jff=JsonFileFactory()
jff.write_data(movie,"../database/Movies.json")