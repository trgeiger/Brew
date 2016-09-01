"""empty message

Revision ID: 143c2c83997c
Revises: None
Create Date: 2016-09-01 11:49:21.712754

"""

# revision identifiers, used by Alembic.
revision = '143c2c83997c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
