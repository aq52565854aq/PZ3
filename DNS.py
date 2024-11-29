import dns.message
import dns.query
import dns.rdataclass
import dns.rdatatype

qname = dns.name.from_text("amazon.com")
q = dns.message.make_query(qname, dns.rdatatype.NS)

print("The query is:")
print(q)
print("")

r = dns.query.udp(q, "192.168.31.159")
print("The response is:")
print(r)

