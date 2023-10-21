from Crypto.Util.number import long_to_bytes
import sympy

c_p = 70770563170413485640234825332830715579644049285355981293505262738914209029517352373077018947770320280278746620671203215024503799950910898732397153179084074098233352980719945417330407037538618730258842372338429001603903091610752262516741188853590089951756761811040256580538917054394236602707893767220570272331
c_q = 13851492318566804426180559171717895114036816324429566434285593612538644178623395941843619351600718862105589158342528216101368809170495598383990497387251379469346455961514711553702647806756877972791529391358173595919397389755049646932111264878041754835352170573649918876911510785389021472942167961552938040890
N = 19694268725205416932271364425385420707850329840157673295273677195054630515982058976079498206887037469237238398405928480684350200120501078231388088496277582527947938156849419785864562896382735306087325118435609429713312673380764412264707904939485238218886677027240033716280913510048689954579551621705920549746909058000987771268371934823850223213735201866888065931847369642802547725217919776237783287489769890109322726430755322073866327698639461994686267421903262258256777595366148454467865658097293146857749360141451451546041703858527691932299750797762597565953059522307802045384870886086792768277420112890024197381341
phi = 19694268725205416932271364425385420707850329840157673295273677195054630515982058976079498206887037469237238398405928480684350200120501078231388088496277582527947938156849419785864562896382735306087325118435609429713312673380764412264707904939485238218886677027240033716280913510048689954579551621705920549746628074068680399113370686212746795530576012850939713222911207509162211597032002438837189193853944160004364194868287701610512383924569996771883743351575199994707067296109349832389723176764968511964606092023026149281647383744920057620837615083525637277639792424720226658009593127619853405831534160987224728925500
e = 65537


#Find p and q
#https://crypto.stackexchange.com/questions/5791/why-is-it-important-that-phin-is-kept-a-secret-in-rsa

#Using quadratic equation

# a = 1
# b = -(n + 1 - phi)
# c = n

a = 1
b = -(N + 1 - phi)
c = N

x = sympy.var('x')

result = sympy.solve(a * x ** 2 + b * x + c)

p = int(result[1])
q = int(result[0])

#Find private exponent d
d = pow(e, -1, p-1)

#Decrypt message
m = pow(c_p, d, p)

print(long_to_bytes(m))