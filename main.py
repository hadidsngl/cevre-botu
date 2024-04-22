import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def su(ctx):
    await ctx.send(
        f'Su kirliliği, suyun doğal durumunu bozan ve insan sağlığına, çevreye ve ekosistemlere zarar verebilen maddelerin su kaynaklarına karışması durumudur. Bu kirlilik genellikle endüstriyel atıklar, tarımsal faaliyetlerden kaynaklanan kimyasal gübreler ve pestisitler, evsel atıklar, petrol ürünleri gibi çeşitli kaynaklardan gelir. Su kirliliği, suyun içilebilirliğini, balık ve diğer su yaşamını etkileyebilir, sulama suyu olarak kullanılan suyun kalitesini düşürebilir ve su ekosistemlerinin dengesini bozabilir. Su kirliliğiyle mücadele etmek için su arıtma tesisleri, atık su arıtma sistemleri ve çevresel düzenlemeler gibi önlemler alınır.')


@bot.command()
async def toprak(ctx):
    await ctx.send(
        f'Toprak kirliliği, toprağın doğal yapısını ve işlevselliğini bozan, bitki ve insan sağlığına zarar verebilen maddelerin toprağa karışması durumudur. Toprak kirliliği genellikle endüstriyel faaliyetler, tarımsal kimyasallar, evsel atıklar, petrol ürünleri gibi çeşitli kaynaklardan kaynaklanabilir. Örneğin, kimyasal gübreler, pestisitler, ağır metaller, petrol türevleri, endüstriyel atıklar gibi maddeler toprağa karışarak kirliliğe neden olabilirler.Toprak kirliliği çeşitli etkilere neden olabilir, bunlar arasında tarım verimliliğinin düşmesi, bitki ve hayvan sağlığının etkilenmesi, yeraltı suyunun kirlenmesi, biyoçeşitliliğin azalması ve insan sağlığına zarar veren maddelerin gıda zinciriyle toplumun içine girmesi sayılabilir.Toprak kirliliğiyle mücadele etmek için toprak analizi ve izleme, kirlenmiş bölgelerin temizlenmesi, kirliliği önlemeye yönelik düzenlemeler ve çevresel koruma politikaları gibi önlemler alınır. Ayrıca, sürdürülebilir tarım uygulamaları ve atık yönetimi de toprak kirliliğinin azaltılmasında önemli rol oynar.')


@bot.command()
async def hava(ctx):
    await ctx.send(
        f'Hava kirliliği, atmosferde bulunan ve insan sağlığını, çevreyi ve ekosistemleri olumsuz yönde etkileyen kirleticilerin (partikül madde, gazlar, dumanlar, kimyasal bileşenler vb.) varlığıdır. Hava kirliliğine neden olan kaynaklar arasında endüstriyel tesisler, araç emisyonları, enerji üretimi, tarımsal faaliyetler, evsel ısınma ve atıklar yer alır.Hava kirliliği insan sağlığı üzerinde ciddi etkilere sahiptir. Solunum yolu hastalıkları, astım, kronik obstrüktif akciğer hastalığı (KOAH), kalp ve damar hastalıkları gibi sağlık sorunlarına yol açabilir. Ayrıca, çevreyi ve ekosistemleri de olumsuz etkiler. Bitki örtüsüne, su kaynaklarına, toprağa ve biyoçeşitliliğe zarar verebilir.Hava kirliliğini azaltmak için çeşitli önlemler alınır. Bunlar arasında daha temiz enerji kaynaklarına geçiş, endüstriyel tesislerin emisyonlarını azaltma, araç emisyonlarını kontrol altına alma, atık yakma tesislerinin modernizasyonu, çevresel düzenlemelerin ve politikaların uygulanması gibi önlemler yer alır. Ayrıca, halkın bilinçlendirilmesi ve çevre koruma konusunda farkındalığın artırılması da hava kirliliğinin azaltılmasında önemlidir')


@bot.command()
async def ses(ctx):
    await ctx.send(
        f'Ses kirliliği, çevreyi olumsuz etkileyen ve insan sağlığını tehdit eden aşırı ve istenmeyen seslerin yayılmasıdır. Bu kirlilik genellikle endüstriyel tesisler, trafik, inşaat faaliyetleri, havaalanları, eğlence mekanları gibi çeşitli kaynaklardan kaynaklanır. Yüksek düzeyde ses, uyku bozukluklarına, işitme kaybına, stres, anksiyete, konsantrasyon bozukluğu, iletişim sorunları ve hatta kalp-damar hastalıkları gibi sağlık sorunlarına neden olabilir.Ses kirliliğinin azaltılması için çeşitli önlemler alınabilir. Bu önlemler arasında endüstriyel tesislerin ve ulaşım araçlarının gürültü seviyelerinin kontrol altına alınması, ses yalıtımı ve izolasyonu, şehir planlamasında ses kirliliği göz önünde bulundurulması, çalışma saatlerinin düzenlenmesi ve toplumda farkındalığın artırılması gibi önlemler yer alır. Ayrıca, yasal düzenlemeler ve standartlar da ses kirliliğinin azaltılmasında önemli bir rol oynar')


@bot.command()
async def ışık(ctx):
    await ctx.send(
        f'Işık kirliliği, gece gökyüzünde yıldızların ve diğer astronomik cisimlerin gözlemlenmesini zorlaştıran veya engelleyen, gereksiz ve istenmeyen ışık yayımıdır. Bu kirlilik, genellikle aydınlatma sistemlerinden kaynaklanır ve kentsel alanlarda yoğunlaşır. Aşırı ışık kirliliği ayrıca doğal yaşamı, insan sağlığını ve ekosistemleri de olumsuz etkiler.Işık kirliliğinin etkileri arasında uyku bozuklukları, biyolojik ritimlerin bozulması, göz rahatsızlıkları, hayvan göç yollarının etkilenmesi ve yıldız gözlemciliği gibi faaliyetlerin zorlaşması yer alır. Ayrıca, fazla ışık tüketimi enerji israfına ve ekonomik kayıplara da neden olabilir.Işık kirliliğini azaltmak için çeşitli yöntemler ve politikalar uygulanabilir. Örneğin, düşük ışık seviyelerine sahip, yönlendirilmiş ve enerji tasarruflu aydınlatma sistemlerinin kullanılması, aydınlatma kaynaklarının zamanında kapatılması veya düşük yoğunlukta kullanılması, karanlık alanların korunması için yerel düzenlemelerin yapılması, bilinçlendirme kampanyaları düzenlenmesi gibi önlemler alınabilir. Bu adımlar, ışık kirliliğini azaltarak hem çevreye hem de insan sağlığına olumlu katkıda bulunabilir')


@bot.command()
async def radyoaktif(ctx):
    await ctx.send(
        f'Radyoaktif kirlilik, çevreye zararlı radyoaktif maddelerin yayılması sonucu oluşan kirlilik durumunu ifade eder. Bu kirlilik genellikle nükleer kazalar, nükleer tesislerin işletilmesi ve atık yönetimi gibi nükleer enerji faaliyetleriyle ilişkilidir, ancak radyoaktif maddelerin diğer endüstriyel veya tıbbi uygulamalardan da kaynaklanabilir.Radyoaktif kirlilik ciddi sağlık ve çevresel risklere neden olabilir. Radyoaktif maddelerin vücuda girmesi veya solunması durumunda kanser, genetik bozukluklar ve diğer sağlık sorunlarına yol açabilirler. Ayrıca, çevresel ekosistemlere zarar verebilir, biyoçeşitliliği etkileyebilir ve su, toprak ve hava gibi doğal kaynaklarda kirliliğe yol açabilirler.Radyoaktif kirliliği önlemek veya azaltmak için bir dizi önlem alınabilir. Bu önlemler arasında nükleer tesislerin güvenliği ve denetimi, atık yönetimi ve depolama standartlarının iyileştirilmesi, radyasyonun izlenmesi ve ölçülmesi, nükleer kazalara hazırlık ve müdahale planlarının oluşturulması, nükleer atık taşıma ve depolama süreçlerinin güvenliği gibi önlemler yer alır. Ayrıca, nükleer enerjinin alternatif enerji kaynaklarıyla değiştirilmesi veya daha güvenli ve temiz nükleer teknolojilerin geliştirilmesi gibi stratejiler de radyoaktif kirliliği azaltmada etkili olabilir.')


bot.run('token here')
