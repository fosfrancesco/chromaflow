# The following files are problematic in windows, so we rename them to replace ":" with "," and remove "?".
# error: invalid path 'data/iRealXML/Aguas de Março 1:2.xml'
# error: invalid path 'data/iRealXML/Aguas de Março 2:2.xml'
# error: invalid path 'data/iRealXML/Ain't That A Grand And Glorious Feeling?.xml'
# error: invalid path 'data/iRealXML/Alors? Voila! 2.xml'
# error: invalid path 'data/iRealXML/Am I Blue?.xml'
# error: invalid path 'data/iRealXML/Are You Lonesome Tonight?.xml'
# error: invalid path 'data/iRealXML/Baby, Won't You Please Come Home?.xml'
# error: invalid path 'data/iRealXML/Berimbau : Consolação - In ABC In B In.xml'
# error: invalid path 'data/iRealXML/Do You Ever Think Of Me?.xml'
# error: invalid path 'data/iRealXML/Do You Know What It Means? (Dixieland Tunes).xml'
# error: invalid path 'data/iRealXML/Do You Know What It Means?.xml'
# error: invalid path 'data/iRealXML/Does Jesus Care?.xml'
# error: invalid path 'data/iRealXML/Flee As A Bird To The Mountain  and Oh Didn't He Ramble?.xml'
# error: invalid path 'data/iRealXML/Gee Baby, Ain't I Good To You?.xml'
# error: invalid path 'data/iRealXML/Got A Match? 1.xml'
# error: invalid path 'data/iRealXML/Got A Match?.xml'
# error: invalid path 'data/iRealXML/Have You Met Miss Jones?.xml'
# error: invalid path 'data/iRealXML/How Deep Is Your Love?.xml'
# error: invalid path 'data/iRealXML/How Long Has This Been Going On? 1.xml'
# error: invalid path 'data/iRealXML/How Long Has This Been Going On?.xml'
# error: invalid path 'data/iRealXML/Is That So?.xml'
# error: invalid path 'data/iRealXML/Isn't It Romantic?.xml'
# error: invalid path 'data/iRealXML/Isn't She Lovely?.xml'
# error: invalid path 'data/iRealXML/Meu Deus, meu Deus, Está Extinta a Escravidão?.xml'
# error: invalid path 'data/iRealXML/O Que Será ? (A Flor da Pele).xml'
# error: invalid path 'data/iRealXML/O Que Será ? (À Flor da Pele).xml'
# error: invalid path 'data/iRealXML/Ou Es-Tu Mon Amour? 1.xml'
# error: invalid path 'data/iRealXML/Quand Refleuriront Les Lilas Blancs? 1.xml'
# error: invalid path 'data/iRealXML/Re: Person I Knew.xml'
# error: invalid path 'data/iRealXML/Sem Compromisso : Obsessão (Orquestra Imperial).xml'
# error: invalid path 'data/iRealXML/What Are You Doing New Year's Eve?.xml'
# error: invalid path 'data/iRealXML/What Are You Doing The Rest Of Your Life?.xml'
# error: invalid path 'data/iRealXML/Where Are You?.xml'
# error: invalid path 'data/iRealXML/Who Can I Turn To?.xml'
# error: invalid path 'data/iRealXML/Who's Sorry Now?.xml'
# error: invalid path 'data/iRealXML/Why Do I Love You?.xml'
# error: invalid path 'data/iRealXML/Why Don't You Do Right?.xml'
# error: invalid path 'data/iRealXML/Will You Still Be Mine? 1.xml'
# error: invalid path 'data/iRealXML/Will You Still Be Mine?.xml'
# error: invalid path 'data/iRealXML/Wot's... Uh The Deal?.xml'

from pathlib import Path
folder_path = Path('data/iRealXML')
for file_path in folder_path.iterdir():
    new_name = file_path.name.replace(":", ",").replace("?", "")
    file_path.rename(folder_path / new_name)