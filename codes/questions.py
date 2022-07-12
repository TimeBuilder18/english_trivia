from firebase import F_DB

update_dq = {}
dm = F_DB.child("-N39j7WBtcXL-vkfrti3").get()
for i in dm:
    update_dq.update({i.key():i.val()})
