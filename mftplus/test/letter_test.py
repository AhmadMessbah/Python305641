from mftplus.model.da.da import DataAccess
from mftplus.model.entity.letter import Letter

letter = Letter()

da = DataAccess(Letter)

da.save(letter)