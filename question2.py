def register_party(parties):
    for party in parties:
        party_name = party.get('party_name')
        member_count = party.get('member_count')
        if member_count >= 1000:
            print(f"Party '{party_name}' is registered.")
        else:
            print(f"Party '{party_name}' does not meet the member count requirement.")
            
            last_registered_party_number = 10003318
new_party_reg_number = last_registered_party_number + 1

mk_party = [{'party_name': 'MK party', 'reg_number': new_party_reg_number, 'member_count': 5300}]
register_party(mk_party)

def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
    voter_info[voter_id] = {'name': name, 'voting_district': voting_district, 'has_voted': has_voted}
    
    parties_on_ballot = ["ANC", "DA", "EFF", "IFP", "VF+", "ACDP", "UDM", "COPE", "AIC", "PAC"]
filtered_parties = [party for party in parties_on_ballot if len(party) >= 4]
print(filtered_parties)

filtered_parties_list = list(filter(lambda party: len(party) >= 4, parties_on_ballot))
print(filtered_parties_list)

voters = [{'name': 'Alice', 'registered': True}, {'name': 'Bob', 'registered': False}]
registered_voters = list(filter(lambda voter: voter['registered'], voters))
print(registered_voters)



