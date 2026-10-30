mountains = ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu'] 
mountains.append('Cho Oyu')
mountains.insert(0, 'Annapurna')
del mountains[1]
popped_mount = mountains.pop()
mountains.remove('Annapurna')
mountains.sort()
mountains.reverse()
print(f"Jumlah gunung: {len(mountains)}")
print("List akhir:", mountains)