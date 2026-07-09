# ZZZ Character Header — เลือกโหลดแค่อันเดียว (install ONLY ONE)

ทั้ง 4 ไฟล์ใช้แท็กเดียวกัน `[CHAR|image_url|Name|#hex|faction]` — **ห้ามเปิดพร้อมกัน** เลือกดีไซน์ที่ชอบแล้ว import แค่ไฟล์เดียว:

| ไฟล์ | ดีไซน์ |
|---|---|
| `ZZZ_Header_A_AgentFileTag_Regex.json` | กรอบเอียงสไตล์ agent select + จุด halftone + เส้น lime→orange |
| `ZZZ_Header_B_KnockKnockContact_Regex.json` | รูปกลมขอบเรืองแสง + จุดสถานะ เข้าชุดกับระบบโทรศัพท์ |
| `ZZZ_Header_C_StripeBanner_Regex.json` | ป้ายดำเอียงเต็มความกว้าง + ลายทางสีประจำตัว |
| `ZZZ_Header_D_ZZZMinimal_Regex.json` | ใกล้เคียง Global Header เดิม + ชิป faction สีมะนาว |

**สำคัญ:** ปิด/อย่าใช้ `Global • Header` กับ `Global • Header (URL)` ในแชท ZZZ — แท็ก 4 ช่องจะชนกับ regex 3 ช่องของ Global. ทุกตัวละครในลอร์บุ๊ค ZZZ มีบรรทัด HEADER พร้อมใช้อยู่แล้ว (รูป + สี + สังกัด).
