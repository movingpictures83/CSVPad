class CSVPadPlugin:
   def input(self, filename):
      f = open(filename, 'r')
      self.contents = f.read().strip()

   def run(self):
      # Parse out FEFF, common in CSVs
      while (ord(self.contents[0]) == 65279):
         self.contents = self.contents[1:]
      if (self.contents[0] != ','):
         self.contents = "\"\"," + self.contents
      else:
         self.contents = "\"\"" + self.contents

   def output(self, filename):
      g = open(filename, 'w')
      g.write(self.contents)
