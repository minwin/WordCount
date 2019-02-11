import re 
import operator


def wordcount() :
    
    f = open("wordcount.txt", "r")
    #print(f.read().lower())
    wordle = f.read().lower()
    
    whitelist = set('abcdefghijklmnopqrstuvwxyz \n')
   
    
    wordle = ''.join(filter(whitelist.__contains__, wordle))
    wordlist = wordle.split()
    #print (wordlist)
    
    wordCount = {}
    blacklist = ('time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world', 
                 'life', 'hand', 'part', 'child', 'eye', 'woman', 'place', 
                 'work', 'week', 'case', 'point', 'government', 'company', 
                 'number', 'group', 'problem', 'fact', 'be', 'have', 'do', 
                 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 
                 'think', 'look', 'want', 'give', 'use', 'find', 'tell', 
                 'ask', 'work', 'seem', 'feel', 'try', 'leave', 'call', 
                 'good', 'new', 'first', 'last', 'long', 'great', 'little', 
                 'own', 'other', 'old', 'right', 'big', 'high', 'different', 
                 'small', 'large', 'next', 'early', 'young', 'important', 
                 'few', 'public', 'bad', 'same', 'able', 'prepositions', 
                 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from', 
                 'up', 'about', 'into', 'over', 'after', 'others', 'the', 
                 'and', 'a', 'that', 'i', 'it', 'not', 'he', 'as', 'you', 
                 'this', 'but', 'his', 'they', 'her', 'she', 'or', 'an', 
                 'will', 'my', 'one', 'all', 'would', 'there', 'their',
                 'were','so', 'a', 'a', 'about', 'above', 'across', 'act', 
                 'active', 'activity', 'add', 'afraid', 'after', 'again', 
                 'age', 'ago', 'agree', 'air', 'all', 'alone', 'along', 
                 'already', 'also', 'always', 'am', 'america', 'amount', 'an',
                 'and', 'angry', 'another', 'answer', 'any', 'anyone', 
                 'anything', 'anytime', 'appear', 'apple', 'are', 'area', 
                 'arm', 'army', 'around', 'arrive', 'art', 'as', 'ask', 'at',
                 'attack', 'aunt', 'autumn', 'away', 'b', 'baby', 'back', 
                 'bad', 'bag', 'ball', 'bank', 'base', 'basket', 'bath', 'be',
                 'bean', 'bear', 'beautiful', 'because', 'bed', 'bedroom', 
                 'beer', 'before', 'begin', 'behave', 'behind', 'bell', 
                 'below', 'besides', 'best', 'better', 'between', 'big', 
                 'bird', 'birth', 'birthday', 'bit', 'bite', 'black', 'bleed',
                 'block', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 
                 'boil', 'bone', 'book', 'border', 'born', 'borrow', 'both',
                 'bottle', 'bottom', 'bowl', 'box', 'boy', 'branch', 'brave',
                 'bread', 'break', 'breakfast', 'breathe', 'bridge', 'bright',
                 'bring', 'brother', 'brown', 'brush', 'burn', 'bus', 
                 'business', 'busy', 'but', 'buy', 'by', 'bye', 'c', 'cake',
                 'call', 'came', 'can', 'candle', 'cap', 'car', 'card', 
                 'care', 'careful', 'careless', 'carry', 'case', 'cat', 
                 'catch', 'central', 'century', 'certain', 'chair', 'chance',
                 'chase', 'cheap', 'cheese', 'chicken', 'child', 'children',
                 'chocolate', 'choice', 'choose', 'circle', 'city', 'class', 
                 'clean', 'clear', 'clever', 'climb', 'clock', 'close', 
                 'cloth', 'clothes', 'cloud', 'cloudy', 'coat', 'coffee', 
                 'coin', 'cold', 'collect', 'colour', 'comb', 'come', 
                 'comfortable', 'common', 'complete', 'computer', 'condition',
                 'contact', 'contain', 'continue', 'control', 'cook', 'cool',
                 'copper', 'corn', 'corner', 'correct', 'cost', 'count', 
                 'country', 'course', 'cover', 'crash', 'cross', 'cry', 'c', 
                 'cup', 'cupboard', 'cut', 'd', 'dance', 'dangerous', 'dark', 
                 'daughter', 'day', 'dead', 'deep', 'deer', 'depend', 'desk', 
                 'destroy', 'die', 'different', 'difficult', 'dinner', 
                 'direction', 'dirty', 'discover', 'dish', 'do', 'dog', 
                 'door', 'double', 'down', 'draw', 'dream', 'dress', 
                 'drink', 'drive', 'drop', 'dry', 'duck', 'during', 
                 'dust', 'duty', 'e', 'each', 'ear', 'early', 'earn', 'earth',
                 'east', 'easy', 'eat', 'effect', 'egg', 'eight', 'either', 
                 'electric', 'elephant', 'else', 'empty', 'end', 'enemy', 
                 'enjoy', 'enough', 'enter', 'entrance', 'equal', 'escape',
                 'even', 'evening', 'ever', 'every', 'everybody', 'everyone',
                 'example', 'except', 'excited', 'expect', 'expensive', 
                 'extremely', 'eye', 'f', 'face', 'fact', 'fail', 'fall', 
                 'false', 'family', 'famous', 'far', 'farm', 'fast', 'fat', 
                 'father', 'fault', 'fear', 'feed', 'feel', 'female', 'fever',
                 'few', 'fight', 'fill', 'film', 'find', 'fine', 'finger', 
                 'finish', 'fire', 'first', 'fit', 'five', 'fix', 'flag', 
                 'flat', 'float', 'floor', 'flour', 'flower', 'fly', 'fold',
                 'food', 'fool', 'foot', 'football', 'for', 'force', 
                 'foreign', 'forest', 'forget', 'forgive', 'fork', 'form',
                 'four', 'fox', 'free', 'freedom', 'freeze', 'fresh', 
                 'friend', 'friendly', 'from', 'front', 'fruit', 'full', 
                 'fun', 'funny', 'furniture', 'further', 'future', 'g', 
                 'game', 'garden', 'gate', 'general', 'gentleman', 'get', 
                 'gift', 'give', 'glad', 'glass', 'go', 'goat', 'god', 'gold',
                 'good', 'goodbye', 'grandfather', 'grandmother', 'grass', 
                 'grave', 'great', 'green', 'grey', 'ground', 'group', 'grow',
                 'gun', 'h', 'hair', 'half', 'hall', 'hammer', 'hand', 
                 'happen', 'happy', 'hard', 'hat', 'hate', 'hatred', 'have', 
                 'he', 'head', 'healthy', 'hear', 'heart', 'heaven', 'heavy',
                 'height', 'hello', 'hen', 'her', 'here', 'hers', 'hide', 
                 'high', 'hill', 'him', 'his', 'hit', 'hobby', 'hold', 
                 'hole', 'holiday', 'home', 'hope', 'horse', 'hospital', 
                 'hot', 'hotel', 'hour', 'house', 'how', 'hundred', 'hungry', 
                 'hurry', 'hurt', 'husband', 'i', 'i', 'ice', 'if', 'in', 
                 'inside', 'into', 'introduce', 'invite', 'iron', 'is',
                 'island', 'it', 'its', 'j', 'jelly', 'juice', 'jump', 'just',
                 'k', 'keep', 'key', 'kill', 'kind', 'king', 'kitchen', 
                 'knee', 'knife', 'knock', 'know', 'l', 'ladder', 'lady', 
                 'lamp', 'land', 'last', 'late', 'lately', 'later', 'laugh',
                 'lazy', 'leaf', 'learn', 'leave', 'left', 'leg', 'lend', 
                 'length', 'less', 'lesson', 'let', 'letter', 'library', 
                 'lie', 'life', 'light', 'like', 'line', 'lion', 'lip', 
                 'list', 'listen', 'little', 'live', 'lock', 'lonely', 
                 'long', 'look', 'lose', 'lot', 'love', 'low', 'lower', 
                 'luck', 'm', 'main', 'male', 'man', 'many', 'mark', 'marry',
                 'matter', 'may', 'me', 'meal', 'mean', 'meat', 'medicine', 
                 'meet', 'member', 'men', 'mention', 'middle', 'might', 
                 'milk', 'million', 'mind', 'minute', 'miss', 'mistake', 
                 'mix', 'modern', 'moment', 'money', 'monkey', 'month', 
                 'moon', 'more', 'morning', 'most', 'mother', 'mountain', 
                 'mouth', 'move', 'much', 'music', 'must', 'my', 'n', 'name',
                 'narrow', 'nation', 'nature', 'near', 'nearly', 'neck', 
                 'need', 'needle', 'neighbour', 'neither', 'net', 'never', 
                 'new', 'news', 'newspaper', 'next', 'nice', 'night', 'nine',
                 'no', 'noble', 'noise', 'none', 'nor', 'north', 'nose', 
                 'not', 'nothing', 'notice', 'now', 'number', 'o', 'obey', 
                 'object', 'ocean', 'of', 'off', 'offer', 'office', 'often', 
                 'oil', 'ok', 'o', 'old', 'on', 'one', 'only', 'open', 
                 'opposite', 'or', 'orange', 'order', 'other', 'our', 'out', 
                 'outside', 'over', 'own', 'p', 'pain', 'paint', 'pair', 
                 'pan', 'paper', 'parent', 'park', 'part', 'party', 'pass', 
                 'past', 'path', 'pay', 'peace', 'pen', 'pencil', 'pepper', 
                 'per', 'perfect', 'period', 'person', 'petrol', 'photograph',
                 'piano', 'pick', 'piece', 'pig', 'pin', 'pink', 'place', 
                 'plane', 'plant', 'plastic', 'plate', 'play', 'please', 
                 'pleased', 'plenty', 'pocket', 'point', 'poison', 'police',
                 'polite', 'pool', 'poor', 'popular', 'possible', 'potato', 
                 'pour', 'powerpregnant', 'present', 'press', 'pretty', 
                 'prevent', 'price', 'prince', 'prison', 'prize', 'probably', 
                 'promise', 'proper', 'protect', 'pull', 'punish', 'pupil', 
                 'push', 'put', 'q', 'queen', 'question', 'quick', 'quiet',
                 'quite', 'r', 'radio', 'rain', 'rainy', 'ready', 'real', 
                 'really', 'receive', 'red', 'remember', 'remind', 'remove',
                 'rent', 'repeat', 'rest', 'restaurant', 'result', 'rice', 
                 'rich', 'ride', 'right', 'ring', 'rise', 'road', 'rob', 
                 'rock', 'room', 'round', 'rubber', 'rude', 'rule', 'ruler', 
                 'rush', 's', 'sad', 'safe', 'said', 'sail', 'salt', 'same', 
                 'sand', 'save', 'say', 'science', 'scissors', 'seat', 
                 'second', 'see', 'seem', 'sentence', 'serve', 'set', 'seven',
                 'several', 'sex', 'shade', 'shadow', 'shake', 'sharp', 'she',
                 'sheep', 'sheet', 'shelf', 'shine', 'ship', 'shirt', 'shoe', 
                 'shoot', 'shop', 'short', 'should', 'shoulder', 'shout', 
                 'show', 'sick', 'side', 'silence', 'silly', 'silver', 
                 'similar', 'simple', 'since', 'sing', 'single', 'sink', 
                 'sister', 'sit', 'o', 'old', 'on', 'one', 'only', 'opposite',
                 'or', 'orange', 'order', 'other', 'our', 'out', 'outside',
                 'over', 'own', 'p', 'page', 'pain', 'paint', 'pair', 'pan', 
                 'paper', 'parent', 'park', 'part', 'party', 'pass', 'past',
                 'path', 'pay', 'peace', 'pen', 'pencil', 'pepper', 'per', 
                 'perfect', 'period', 'person', 'petrol', 'photograph', 
                 'piano', 'pick', 'picture', 'piece', 'pig', 'pin', 'pink', 
                 'place', 'plane', 'plant', 'plastic', 'plate', 'play', 
                 'please', 'pleased', 'plenty', 'pocket', 'point', 'poison',
                 'police', 'polite', 'pool', 'poor', 'popular', 'position', 
                 'possible', 'potato', 'pour', 'power', 'pregnant', 'present',
                 'press', 'pretty', 'prevent', 'price', 'prince', 'prison', 
                 'private', 'prize', 'probably', 'problem', 'produce', 
                 'promise', 'proper', 'protect', 'provide', 'public', 'pull', 
                 'punish', 'pupil', 'push', 'put', 'q', 'queen', 'quick', 
                 'quiet', 'quite', 'r', 'radio', 'rain', 'rainy', 'read', 
                 'ready', 'real', 'really', 'receive', 'record', 'red', 
                 'remember', 'remind', 'remove', 'rent', 'repair', 'repeat', 
                 'reply', 'report', 'rest', 'restaurant', 'result', 'return', 
                 'rice', 'rich', 'ride', 'right', 'ring', 'rise', 'road', 
                 'rob', 'rock', 'room', 'round', 'userrualeave', 'rubber', 
                 'rude', 'rule', 'ruler', 'run', 'rush', 's', 'sad', 'safe', 
                 'said', 'sail', 'salt', 'same', 'sand', 'save', 'say', 
                 'school', 'science', 'scissors', 'search', 'seat', 'second',
                 'see', 'seem', 'sell', 'send', 'sentence', 'serve', 'set', 
                 'seven', 'several', 'sex', 'shade', 'shadow', 'shake', 
                 'shape', 'share', 'sharp', 'she', 'sheep', 'sheet', 'shelf',
                 'shine', 'ship', 'shirt', 'shoe', 'shoot', 'shop', 'short',
                 'should', 'shoulder', 'shout', 'show', 'sick', 'side', 
                 'signal', 'silence', 'silly', 'silver', 'similar', 'simple',
                 'since', 'sing', 'single', 'sink', 'sister', 'sit', 'o', 
                 'old', 'on', 'one', 'only', 'open', 'opposite', 'or', 
                 'orange', 'order', 'other', 'our', 'out', 'outside', 'over', 
                 'own', 'p', 'page', 'pain', 'paint', 'pair', 'pan', 'paper', 
                 'parent', 'park', 'part', 'partner', 'party', 'pass', 'past',
                 'path', 'pay', 'peace', 'pen', 'pencil', 'people', 'pepper', 
                 'per', 'perfect', 'period', 'person', 'petrol', 'photograph',
                 'piano', 'pick', 'picture', 'piece', 'pig', 'pin', 'pink', 
                 'place', 'plane', 'plant', 'plastic', 'plate', 'play', 
                 'please', 'pleased', 'plenty', 'pocket', 'point', 'poison',
                 'police', 'polite', 'pool', 'poor', 'popular', 'position', 
                 'possible', 'potato', 'pour', 'power', 'pregnant', 'present',
                 'press', 'pretty', 'prevent', 'price', 'prince', 'prison', 
                 'private', 'prize', 'probably', 'problem', 'produce', 
                 'promise', 'proper', 'protect', 'provide', 'public', 'pull', 
                 'punish', 'pupil', 'push', 'put', 'q', 'queen', 'question', 
                 'quick', 'quiet', 'quite', 'r', 'radio', 'rain', 'rainy', 
                 'raise', 'reach', 'read', 'ready', 'real', 'really', 
                 'receive', 'record', 'red', 'remember', 'remind', 'remove',
                 'rent', 'repair', 'repeat', 'reply', 'report', 'rest', 
                 'restaurant', 'result', 'return', 'rice', 'rich', 'ride', 
                 'right', 'ring', 'rise', 'road', 'rob', 'rock', 'room', 
                 'round', 'userrualeave', 'rubber', 'rude', 'rule', 'ruler',
                 'run', 'rush', 's', 'sad', 'safe', 'said', 'sail', 'salt', 
                 'same', 'sand', 'save', 'say', 'school', 'science', 
                 'scissors', 'search', 'seat', 'second', 'see', 'seem', 
                 'sell', 'send', 'sentence', 'serve', 'set', 'seven', 
                 'several', 'sex', 'shade', 'shadow', 'shake', 'shape', 
                 'share', 'sharp', 'she', 'sheep', 'sheet', 'shelf', 'shine', 
                 'ship', 'shirt', 'shoe', 'shoot', 'shop', 'short', 'should', 
                 'shoulder', 'shout', 'show', 'sick', 'side', 'signal',
                 'silence', 'silly', 'silver', 'similar', 'simple', 'since',
                 'sing', 'single', 'sink', 'sister', 'sit', 's', 'six', 
                 'size', 'skill', 'skin', 'skirt', 'sky', 'sleep', 'slip', 
                 'slow', 'small', 'smell', 'smile', 'smoke', 'snow', 'so', 
                 'soap', 'sock', 'soft', 'some', 'someone', 'something', 
                 'sometimes', 'son', 'soon', 'sorry', 'sound', 'soup', 
                 'south', 'space', 'speak', 'special', 'speed', 'spell', 
                 'spend', 'spoon', 'sport', 'spread', 'spring', 'square', 
                 'stamp', 'stand', 'star', 'start', 'station', 'stay', 
                 'steal', 'steam', 'step', 'still', 'stomach', 'stone', 
                 'stop', 'store', 'storm', 'story', 'strange', 'street', 
                 'strong', 'structure', 'student', 'study', 'stupid', 
                 'subject', 'substance', 'successful', 'such', 'sudden',
                 'sugar', 'suitable', 'summer', 'sun', 'sunny', 'support', 
                 'sure', 'surprise', 'sweet', 'swim', 'sword', 't', 'table', 
                 'take', 'talent', 'talk', 'tall', 'taste', 'taxi', 'tea', 
                 'teach', 'team', 'tear', 'telephone', 'television', 'tell',
                 'ten', 'tennis', 'terrible', 'test', 'than', 'that', 'the',
                 'their', 'then', 'there', 'therefore', 'these', 'they', 
                 'thick', 'thin', 'thing', 'think', 'third', 'this', 
                 'though', 'thought', 'threat', 'three', 'through', 'tidy',
                 'tie', 'title', 'to', 'today', 'toe', 'together', 'tomorrow',
                 'tonight', 'too', 'tool', 'tooth', 'top', 'total', 'touch',
                 'town', 'train', 'tram', 'travel', 'tree', 'trouble', 'true',
                 'trust', 'try', 'turn', 'twice', 'two', 'type', 'u', 'uncle',
                 'under', 'understand', 'unit', 'until', 'up', 'us', 'use', 
                 'useful', 'usual', 'usually', 'v', 'vegetable', 'very', 
                 'village', 'visit', 'voice', 'w', 'wait', 'wake', 'walk', 
                 'want', 'warm', 'was', 'wash', 'waste', 'watch', 'water', 
                 'way', 'we', 'weak', 'wear', 'weather', 'wedding', 'week', 
                 'weight', 'welcome', 'well', 'went', 'were', 'west', 'wet',
                 'what', 'wheel', 'when', 'where', 'which', 'while', 'white',
                 'who', 'why', 'wide', 'wife', 'wild', 'will', 'win', 'wind', 
                 'window', 'wine', 'winter', 'wire', 'wise', 'wish', 'with', 
                 'without', 'woman', 'wonder', 'word', 'work', 'world', 
                 'worry', 'worst', 'would', 'write', 'wrong', 'y', 'year',
                 'yes', 'yesterday', 'yet', 'you', 'young', 'your', 'z', 
                 'zero', 'zoo')
    
    
    
    
    for word in wordlist:
        #print (word)
        if word in blacklist:
            continue
            
        if word in wordCount:
            wordCount[word] += 1    
        else:
            wordCount[word]=1
            
    #print (wordCount)
    
    sorted_WC = sorted(wordCount.items(), key=operator.itemgetter(1))
    for row in sorted_WC:
        print ("%s,%s" % (row[0] , row[1]) )