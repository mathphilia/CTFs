def root(x, n):
    # return n-th root of x
    digits = x.bit_length() // n
    ans = 0
    for i in range(digits, -1, -1):
        ans ^= 1 << i
        if x < ans ** n:
            ans ^= 1 << i
    return ans

def xor(cip, key):
        repeation = 1 + (len(cip) // len(key))
        key = key * repeation
        key = key[:len(cip)]

        msg = bytes([c ^ k for c, k in zip(cip, key)])
        return msg

def summarize(b):
    return root((b - 1) ** 3, 2) * 2 // 3 + root(b - 1, 2)


c0 = 194487778980461745865921475300460852453586088781074246328543689440168930873549359227127363759885970436167330043371627413542337857082400024590112412164095470165662281502211335756288082198009158469871465280749846525326701136380764079685636158337203211609233704905784093776008350120607841177268965738426317288541638374141671346404729428158104872411498098187946543666987926130124245185069569476433120128275581891425551325847219504501925282012199947834686225770246801353666030075146469275695499044424390475398423700504158154044180028733800154044746648133536737830623670383925046006108348861714435567006327619892239876863209887013290251890513192375749866675256952802329688897844132157098061758362137357387787072005860610663777569670198971946904157425377235056152628515775755249828721767845990597859165193162537676147173896835503209596955703313430433124688537275895468076469102220355973904702901083642275544954262724054693167603475188412046722656788470695566949847884250306735314144182029335732280420629131990311054229665691517003924788583771265625694414774865289407885678238795596912006567817508035434074250123869676396153982762032750080222602796273083162627489526255501643913672882350236497429678928099868244687228703074267962827621792960
c1 = 102325064080381160170299055162846304227217463467232681115953623386548494169967745781550171804781503102663445039561476870208178139548389771866145006535051362059443515034504958703659546162037904784821960707630188600064568878674788077706711506213779443920430038560373854184526850365974450688458342413544179732143225845085164110594063440979455274250021370090572731855665413325275414458572412561502408983107820534723804225765540316307539962199024757378469001612921489902325166003841336027940632451584642359132723894801946906069322200784708303615779699081247051006259449466759863245508473429631466831174013498995506423210088549372249221415401309493511477847517923201080509933268996867995533386571564898914042844521373220497356837599443280354679778455765441375957556266205953496871475611269965949025704864246188576674107448587696941054123618319505271195780178776338475090463487960063464172195337956577785477587755181298859587398321270677790915227557908728226236404532915215698698185501562405374498053670694387354757252731874312411228777004316623425843477845333936913444143768519959591070492639650368662529749434618783626718975406802741753688956961837855306815380844030665696781685152837849982159679122660714556706669865596780528277684800454866433826417980212164051043504955615794706595412705883261111953152250227679858538249797999044336210905975316421254442221408945203647754303635775048438188044803368249944201671941949138202928389951227347433255867504906597772044398973241425387514239164853656233776024571606159378910745571588836981735827902305330330946219857271646498602227088657739442867033212012876837654750348578740516798444734534291467314881324902354425889448102902750077077381896216130734894767553834949561471219923459897244690006643798812989271282475503126962274052192342840870308710338336817452628324667507548265612892611100350882163205858101959976
enc = 122235247669762131006183252122503937958296387791525458429403709404875223067116491817728568224832483391622109986550732469556761300197133827976956875865159629512476600711420561872409721582387803219651736262581445978042694384374119142613277808898398213602093802571586386354257378956087240174787723503606671543195193114158641301908622673736098768829071270132073818245595918660134745516367731595853832524328488074054536278197115937409643221809577554866060292157239061557708159310445977052686561229611117673473208278176118561352693319461471419694590218295911647368543698198762827636021268989705079848502749837879584394379300566277359149621932579222865430374652678738198451655509408564586496375811666876030847654260305392984710580761255795785508407844683687773983669843744274915862335181251050775093896006210092665809300090715190088851654138383362259256212093670748527819287681468901379286722214112321906917311154811516336259463356911326393701445497605365038857575515541024824906818473933597129846235905072394148879079996812146836910199111439031562946495046766063326815863624262541346543552652673629442370320109404700346028639853707278295255350982238521659924641921142615894039995513480511108116053798143154593343124822462519555715118822045

P_plus_Q = root(c1, 3)
P_minus_Q = c0 // P_plus_Q
P = (P_plus_Q + P_minus_Q) // 2
Q = (P_plus_Q - P_minus_Q) // 2

n = P * Q
phi = (P - 1) * (Q - 1)
e = 0x10001
d = pow(e, -1, phi)
m = pow(enc, d, n)
enc0 = m.to_bytes((m.bit_length() + 7) // 8, 'big')

_xor_key = summarize(n)
xor_key = _xor_key.to_bytes((_xor_key.bit_length() + 7) // 8, 'big')[:512]
padded_msg = xor(enc0, xor_key)
print(padded_msg.decode(errors = 'replace'))