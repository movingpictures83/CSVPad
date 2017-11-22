class CSVPadPlugin:
   def input(self, filename):
      f = open(filename, 'r')
      self.contents = f.read()

   def run(self):
      self.contents = "\"\"," + self.contents

   def output(self, filename):
      g = open(filename, 'w')
      g.write(self.contents)
