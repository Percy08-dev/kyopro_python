
n = int(input())
m_n = ["",""]
m_h = [0, 0]

for i in range(n):
    s, t = map(str, input().split())
    t = int(t)
    if m_h[0] < t:
        m_h[1] = m_h[0]
        m_n[1] = m_n[0]
        m_h[0] = t
        m_n[0] = s
    elif m_h[1] < t:
        m_h[1] = t
        m_n[1] = s

print(m_n[1])