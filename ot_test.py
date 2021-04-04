def __ot__():
  p = 2**32 - 1						#Zp
  g = random_p(0,p)				#group element
  b = assign(with_player="player_0", console, range(0,1))			#让player_0输入b ∊ Z_2
  x = assign(with_player="player_1", console, type="array", shape = (2,))#让player_1输入x ∊ {Z_p}^2
  c = random_p(0,p)
  with assign(with_player="player_1"):
    k = random_p(p)
    pk = pow(g, k, nodule = p)
    pk0,pk1 = [pk, div(c, pk)] if b == 0 else [div(c, pk), pk]
  	net.send([pk0,pk1,c], from_player = "player_1", to_player = "player_0")
  with assign(with_player="player_0"):
    check(c == mul(pk0,pk1))
    r0,r1 = random_p(p, shape = (2,))
    e0 = ["h":pow(g, r0, p), "s":xor(Hash("sha-2", pow(pk0, r0, p)),x0)]
    e1 = ["h":pow(g, r1, p), "s":xor(Hash("sha-2", pow(pk1, r1, p)),x1)]
    net.send([e0,e1], from_player = "player_0", to_player = "player_1")
  with assign(with_player="player_1"):
    e = e0 if b == 0 else e1
    x = Hash("sha-2", xor(pow(e["h"], k, p),e["s"]))