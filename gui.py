import tkinter as tk
from tkinter import ttk
import random

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Karakter Sınır Girişi")
        self.root.geometry("800x400")
        
        self.bg_color = "#2e1f1f"        # Koyu kestane zemin
        self.frame_bg = "#3b2f2f"        # Hafif açık çerçeve
        self.text_color = "#f5f5dc"      # Açık krem yazı
        self.entry_bg = "#4b3832"        # Sıcak kahve entry
        self.button_bg = "#d2691e"       # Tarçın-turuncu buton
        self.button_fg = "#ffffff"       # Beyaz yazı






        

        self.root.configure(bg=self.bg_color)
        
        self.reversedDataList = []

        
        top1 = tk.Frame(root, bg=self.frame_bg)
        top1.pack(padx=10, pady=10, anchor="w")

        label_bit = tk.Label(top1, text="Data Uzunluğu:", bg=self.frame_bg, fg=self.text_color)
        label_bit.pack(side="left", padx=(0,10))

        self.bitNumberArray = [8, 16, 32]
        self.chosenBitNumber = tk.StringVar()
        self.comboBox = ttk.Combobox(top1, textvariable=self.chosenBitNumber, values=self.bitNumberArray, state="readonly", width=5)
        self.comboBox.pack(side="left")
        self.comboBox.current(0)

        
        top2 = tk.Frame(root, bg=self.frame_bg)
        top2.pack(padx=10, pady=10, anchor="w")

        label_data = tk.Label(top2, text="Data:", bg=self.frame_bg, fg=self.text_color)
        label_data.pack(side="left", padx=(0,10))

        
        def validate_binary(P):
            if P == "":  
                return True
            if all(c in '01' for c in P):  
                return True
            return False
        
        vcmd = (self.root.register(validate_binary), '%P')

        self.dataInput = tk.StringVar()
        self.entry = tk.Entry(top2, textvariable=self.dataInput, width=40, validate='key', validatecommand=vcmd, bg=self.entry_bg, fg=self.text_color, insertbackground=self.text_color)
        self.entry.pack(side="left")

        self.encode_button = tk.Button(top2, text="Encode", command=self.encode_action, bg=self.button_bg, fg=self.button_fg)
        self.encode_button.pack(side="left", padx=10)

        self.dataInput.trace_add("write", self.dataLimit)

        
        middle1 = tk.Frame(root, bg=self.frame_bg)
        middle1.pack(padx=10, pady=20, anchor="w")

        label_hamming = tk.Label(middle1, text="Hamming Code:", bg=self.frame_bg, fg=self.text_color)
        label_hamming.pack(side="left", pady=5)

        self.hamming_entry = tk.Entry(middle1, width=50, state='readonly', bg=self.entry_bg, fg=self.text_color, readonlybackground=self.entry_bg)
        self.hamming_entry.pack(side="left", padx=(10,0))
        
        middle2 = tk.Frame(root, bg=self.frame_bg)
        middle2.pack(padx=10, pady=10, anchor="w")

        self.single_error_button = tk.Button(middle2, text="Tek Hata Ekle", width=16, height=3, command=self.oneErrorButtonAction, bg=self.button_bg, fg=self.button_fg)
        self.single_error_button.pack(side="left", padx=(0,10))

        self.double_error_button = tk.Button(middle2, text="Çift Hata Ekle", width=16, height=3, command=self.twoErrorButtonAction, bg=self.button_bg, fg=self.button_fg)
        self.double_error_button.pack(side="left", padx=(0,10))

        
        manual_error_frame = tk.Frame(middle2, bg=self.frame_bg)
        manual_error_frame.pack(side="left", padx=(0,10))
        
        
        def validate_number(P):
            if P == "": 
                return True
            if P.isdigit():  
                return True
            return False
        
        vcmd = (self.root.register(validate_number), '%P')
        
        self.manual_error_entry = tk.Entry(manual_error_frame, width=5, validate='key', validatecommand=vcmd, bg=self.entry_bg, fg=self.text_color, insertbackground=self.text_color)
        self.manual_error_entry.pack(side="left", padx=(0,5))
        
        self.manual_error_button = tk.Button(manual_error_frame, text="İndex'e Hata Ekle", 
                                           width=16, height=3, command=self.manualErrorButtonAction, bg=self.button_bg, fg=self.button_fg)
        self.manual_error_button.pack(side="left")

        
        self.error_label = tk.Label(middle2, text="", fg=self.text_color, bg=self.frame_bg)
        self.error_label.pack(side="left", padx=20)
        
        
        bottom = tk.Frame(root, bg=self.frame_bg)
        bottom.pack(padx=10, pady=10, anchor="w")
        
        self.controlB = tk.Button(bottom, text="Kontrol", width=16, height=3, command=self.control_action, bg=self.button_bg, fg=self.button_fg)
        self.controlB.pack(side="left", padx=(0,10))
        
        
        self.fix_button = tk.Button(bottom, text="Düzelt", width=16, height=3, command=self.fix_error, fg="green", bg=self.button_bg)
        self.fix_button.pack(side="left", padx=(0,10))
        self.fix_button.pack_forget()  
        
        self.error_position = None  
    def dataLimit(self, *args):
        try:
            limit = int(self.chosenBitNumber.get())
        except ValueError:
            limit = 8

        current_text = self.dataInput.get()
        if len(current_text) > limit:
            current_text = current_text[:limit]
            self.dataInput.set(current_text)

        self.reversedDataList.clear()
        for ch in reversed(current_text):
            self.reversedDataList.append(ch)
        self.hamming_generator()



    def hamming_generator(self):
        tp=0
        checkPositions=[]

        m = len(self.reversedDataList)
        p = 0
        while (2 ** p) < (m + p + 1):
            p += 1
        for i in range(p):
            checkPositions.append(2**i)

        
        """
            for i in range(m+p):
                if i in checkPositions:
                    if hammingList[i]==1:
                        if i ==1:

                            
                        elif i ==2:
                            
                        elif i ==4:
                            
                        elif i ==8:
                            
                        elif i ==16:
                        
                        elif i ==32:
                        
                        bu yaklaşım uzun sürebilr""" 

        hammingList = [0] * (m+p+1)  
        dataIndex=0
        for i in range(1,m+p+1):
            if i not in checkPositions:
                hammingList[i]=int(self.reversedDataList[dataIndex]) 
                dataIndex +=1



        for parityPos in checkPositions: 
            parity = 0
        
            i = parityPos
            while i <= m + p:
                block = hammingList[i:i+parityPos]
                parity ^= sum(block) % 2
                i += 2 * parityPos
            hammingList[parityPos] = parity

        globalParity = sum(hammingList[1:]) % 2
        hammingList.append(globalParity)


        self.hammingListLast=hammingList[1:]
        self.reversedHammngListLast = self.hammingListLast[::-1]




    def encode_action(self):
        self.hamming_entry.configure(state='normal')
        self.hamming_entry.delete(0, tk.END)
        hamming_str = ''.join(str(bit) for bit in self.hammingListLast)
        self.hamming_entry.insert(0, hamming_str)
        self.hamming_entry.configure(state='readonly')
        self.error_label.config(text="")

    def oneErrorButtonAction(self):
        if not hasattr(self, "hammingListLast") or not self.hammingListLast:
            self.error_label.config(text="Önce veri girip encode edin.")
            return
        
        length = len(self.hammingListLast)
        error_index = random.randint(0, length-1)
        
        
        self.hammingListLast[error_index] = 1 - self.hammingListLast[error_index]

        self.updateHamming_Error()
        self.error_label.config(text=f"{error_index} indisinde hata oluşturuldu")


    def twoErrorButtonAction(self):
        if not hasattr(self, "hammingListLast") or not self.hammingListLast:
            self.error_label.config(text="Önce veri girip encode edin.")
            return
        
        length = len(self.hammingListLast)
        if length < 2:
            self.error_label.config(text="Yeterli uzunlukta veri yok.")
            return
        

        error_indices = random.sample(range(length), 2)
        
        
        for idx in error_indices:
            self.hammingListLast[idx] = 1 - self.hammingListLast[idx]

        self.updateHamming_Error()
        self.error_label.config(text=f"{error_indices[0]},{error_indices[1]} indisinde hata oluşturuldu")
    
    def updateHamming_Error(self):
        self.hamming_entry.configure(state='normal')
        self.hamming_entry.delete(0, tk.END)
        hamming_str = ''.join(str(bit) for bit in self.hammingListLast)
        self.hamming_entry.insert(0, hamming_str)
        self.hamming_entry.configure(state='readonly')

    def control_action(self):
        if not hasattr(self, "hammingListLast") or not self.hammingListLast:
            self.error_label.config(text="Önce veri girip encode edin.")
            return

        
        self.fix_button.pack_forget()
        self.error_position = None

        hammingText = self.hamming_entry.get()
        hammingArray = [int(bit) for bit in hammingText]
        n = len(hammingArray) - 1  
        p = 0
        while (2 ** p) < n + 1:
            p += 1

        checkPositions = [2 ** i for i in range(p)]

        
        syndrome = 0
        for parityPos in checkPositions:
            parity = 0
            i = parityPos
            while i <= n:
                block = hammingArray[i-1 : min(i-1 + parityPos, n)]
                parity ^= sum(block) % 2
                i += 2 * parityPos

            if parity != 0:
                syndrome += parityPos

        
        globalParityBit = hammingArray[-1]
        calculatedGlobalParity = sum(hammingArray[:-1]) % 2
        globalParityError = (calculatedGlobalParity != globalParityBit)

        
        if syndrome == 0 and not globalParityError:
            
            self.error_label.config(text="Hata yok.")
        elif syndrome != 0 and globalParityError:
            
            self.error_label.config(text=f"Tek hata bulundu! Hatalı bit pozisyonu: {syndrome-1}")
            
            self.error_position = syndrome
            self.fix_button.pack(side="left", padx=(0,10))
        elif  (syndrome != 0 and not globalParityError):
            
            self.error_label.config(text="Çift hata tespit edildi!")
        elif (syndrome == 0 and globalParityError):
            self.error_label.config(text="Tek hata tespit edildi!")
            self.error_position = syndrome
            self.fix_button.pack(side="left", padx=(0,10))
        else:
            self.error_label.config(text="Bilinmeyen hata durumu.")

        
        self.hamming_entry.configure(state='normal')
        self.hamming_entry.delete(0, tk.END)
        hamming_str = ''.join(str(bit) for bit in hammingArray)
        self.hamming_entry.insert(0, hamming_str)
        self.hamming_entry.configure(state='readonly')

    def fix_error(self):
        if self.error_position is not None:
        
            hammingText = self.hamming_entry.get()
            hammingArray = [int(bit) for bit in hammingText]
            
        
            error_idx = self.error_position - 1  
            if error_idx < len(hammingArray):
                hammingArray[error_idx] = 1 - hammingArray[error_idx]
            
           
            self.hammingListLast = hammingArray
            self.updateHamming_Error()
            
          
            self.error_label.config(text="Hata düzeltildi!")
            self.fix_button.pack_forget()
            self.error_position = None

    def manualErrorButtonAction(self):
        if not hasattr(self, "hammingListLast") or not self.hammingListLast:
            self.error_label.config(text="Önce veri girip encode edin.")
            return
            
        try:
            error_index = int(self.manual_error_entry.get())
            if error_index < 0 or error_index >= len(self.hammingListLast):
                self.error_label.config(text=f"Geçersiz index! 0-{len(self.hammingListLast)-1} arası bir değer girin.")
                return
                
         
            self.hammingListLast[error_index] = 1 - self.hammingListLast[error_index]
            
            self.updateHamming_Error()
            self.error_label.config(text=f"{error_index} indisinde hata oluşturuldu")
            
        except ValueError:
            self.error_label.config(text="Lütfen geçerli bir sayı girin!")

if __name__ == "__main__":
    root = tk.Tk() 
    app = GUI(root)
    root.mainloop()
